console.log("=====DLP roundcube extension loaded=====");

// let policyState = "NO_ATTACHMENT";

// document.addEventListener("change", async (event) => {
//     const element = event.target;
//     if (element.tagName !== "INPUT") {
//         return;
//     }
//     if (element.tagName !== "file") {
//         return;
//     }
//     policyState = "SCANNING";
//     for (const file of element.files) {
//         console.log("=====DLP attachment detected by content.js=====");
//         console.log("fileName: ", file.name);
//         console.log("fileType: ", file.type);
//         console.log("fileSize: ", file.size);
//         console.log("file:");
//         console.log(file);

//         const data = {
//             fileName: file.name,
//             fileType: file.Type,
//             fileSize: file.size,
//             fileContent: file,
//         };

//         chrome.runtime.sendMessage(
//             {
//                 type: "get_file_info",
//                 data: data,
//             },
//             (response) => {
//                 console.log("response received by background.js: ", response);
//             }
//         );
//     }
// });

let policyState = "NO_ATTACHMENT";

document.addEventListener(
    "change",
    (event) => {
        console.log("change event triggered!");
        console.log("event.target: ", event.target);
        console.log("it's tagname is:", event.target.tagName);
        console.log("it's type is:", event.target.type);

        const element = event.target;

        if (element.tagName !== "INPUT") {
            return;
        }
        if (element.type !== "file") {
            return;
        }
        policyState = "SCANNING";
        try {
            console.log("executing try block");
            console.log("element.files:", element.files);
            console.log("len of element.files:", element.files.length);
            for (const file of element.files) {
                console.log("=====DLP attachment detected by content.js=====");
                console.log("fileName is:", file.name);
                console.log("fileSize is:", file.size);
                console.log("fileType is:", file.type);
                console.log("file is:", file);
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
                        console.log(
                            "response received from background.js is:",
                            response,
                        );
                        console.log("response type:", typeof response);
                        console.log("response.success:", response.success);
                        if (response.success) {
                            if (response.policy_response.allowed === true) {
                                policyState = "ALLOW";
                                console.log(
                                    "response.policy_response.allowed:",
                                    response.policy_response.allowed,
                                );
                            } else if (
                                response.policy_response.allowed === false
                            ) {
                                policyState = "DENY";
                                console.log(
                                    "response.policy_response.allowed:",
                                    response.policy_response.allowed,
                                );
                            }
                        }
                    },
                );
            }
        } catch (error) {
            console.error("caught error:", error.stack);
        }
    },
    true,
);

document.addEventListener(
    "click",
    (event) => {
        console.log("click event triggered");
        const sendButton = event.target.closest(".send");
        if (!sendButton) {
            return;
        }
        console.log("send button click event triggered");
        console.log("event.target:", event.target);
        console.log("event.type:", event.type);
        console.log("sendButton:", sendButton);
        if (policyState == "SCANNING") {
            console.log("DLP: scanning in progress");
            event.preventDefault();
            event.stopPropagation();
            event.stopImmediatePropagation();
            alert("scanning in progress");
            return;
        } else if (policyState == "ALLOW") {
            console.log("DLP: send allowed");
            return;
        } else if (policyState == "DENY") {
            console.log("DLP: send operation is blocked!");
            event.preventDefault();
            event.stopPropagation();
            event.stopImmediatePropagation();
            alert("you do not have permission to send these files");
            return;
        } else if (policyState == "NO_ATTACHMENT") {
            console.log("no attachment - allowed");
            return;
        }
    },
    true,
);
