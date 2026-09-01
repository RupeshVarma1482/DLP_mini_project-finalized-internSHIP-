// console.log("DLP Gmail extension loaded");

// document.addEventListener("change", function (event) {
//     const element = event.target;

//     if (element.tagName !== "INPUT") {
//         return;
//     }

//     if (element.type !== "file") {
//         return;
//     }

//     for (const file of element.files) {
//         console.log("===== DLP ATTACHMENT DETECTED =====");
//         console.log("Filename:", file.name);
//         console.log("Size:", file.size);
//         console.log("Type:", file.type);

//         const data = {
//             filename: file.name,
//             size: file.size,
//             type: file.type,
//         };

//         chrome.runtime.sendMessage({
//             type: "get_file_info",
//             data: data,
//         });
//     }
// });

console.log("=====DLP gmail extension loaded=====");

let policyState = "NO_ATTACHMENT";

document.addEventListener("change", async (event) => {
    const element = event.target;
    if (element.tagName !== "INPUT") {
        return;
    }
    if (element.type !== "file") {
        return;
    }
    policyState = "SCANNING";
    for (const file of element.files) {
        console.log("===== DLP attachment detected by content.js =====");
        console.log(`filename: ${file.name}`);
        console.log(`filetype: ${file.type}`);
        console.log(`filesize: ${file.size}`);
        console.log(`file:`);
        console.log(file);

        const data = {
            fileName: file.name,
            fileType: file.type,
            fileSize: file.size,
            fileContent: file,
        };
        chrome.runtime.sendMessage(
            {
                type: "get_file_info",
                data: data,
            },
            (response) => {
                console.log(`response received:`, response);
                console.log(`response type:`, typeof response);
                console.log(`response.success:`, response.success);
                if (response.success) {
                    if (response.policy_response.allowed === true) {
                        policyState = "ALLOW";
                        console.log(
                            `response.policy_response.allowed`,
                            response.policy_response.allowed,
                        );
                    } else if (response.policy_response.allowed === false) {
                        policyState = "DENY";
                        console.log(
                            `response.policy_response.allowed`,
                            response.policy_response.allowed,
                        );
                    }
                }
            },
        );
    }
});

document.addEventListener(
    "click",
    (event) => {
        console.log(`click event triggered`);
        const sendButton = event.target.closest(
            '[role="button"][aria-label*="Send"]',
        );
        if (!sendButton) {
            return;
        }
        // policyState is technically ->
        // {"allowed":false,
        // reason":"prohibited word found in TXT/CSV file"}
        if (policyState == "SCANNING") {
            console.log("DLP: scanning in progress");
            event.preventDefault();
            event.stopPropagation();
            event.stopImmediatePropagation();
            alert(`scanning in progress`);
            return;
        } else if (policyState == "ALLOW") {
            console.log("DLP: send allowed");
            return;
        } else if (policyState == "DENY") {
            console.log("DLP: send operation is blocked!!!");
            event.preventDefault();
            event.stopPropagation();
            event.stopImmediatePropagation();
            alert(`you do not have permission to send these files`);
            return;
        } else if (policyState == "NO_ATTACHMENT") {
            console.log("no attachment - allowed");
            return;
        }
    },
    true,
);
