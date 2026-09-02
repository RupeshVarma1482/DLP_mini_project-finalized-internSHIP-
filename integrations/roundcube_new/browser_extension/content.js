console.log("=====DLP roundcube extension loaded=====");

let policyState = "NO_ATTACHMENT";

document.addEventListener("change", async (event) => {
    const element = event.target;
    if (element.tagName !== "INPUT") {
        return;
    }
    if (element.tagName !== "file") {
        return;
    }
    policyState = "SCANNING";
    for (const file of element.files) {
        console.log("=====DLP attachment detected by content.js=====");
        console.log("fileName: ", file.name);
        console.log("fileType: ", file.type);
        console.log("fileSize: ", file.size);
        console.log("file:");
        console.log(file);

        const data = {
            fileName: file.name,
            fileType: file.Type,
            fileSize: file.size,
            fileContent: file,
        };

        chrome.runtime.sendMessage(
            {
                type: "get_file_info",
                data: data,
            },
            (response) => {
                console.log("response received by background.js: ", response);
                
            }
        );
    }
});
