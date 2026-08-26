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

document.addEventListener("change", (event) => {
    const element = event.target;
    if (element.tagName !== "INPUT") {
        return
    }
    if (element.type !== "file") {
        return
    }
    for (const file of element.files) {
        console.log("===== DLP attachment detected by content.js =====");
        console.log(`filename: ${file.name}`);
        console.log(`filetype: ${file.type}`);
        console.log(`filesize: ${file.size}`);
        const data = {
            "filename" : file.name,
            "filetype" : file.type,
            "filesize" : file.size
        };
        chrome.runtime.sendMessage({
            "type" : "get_file_info",
            "data" : data
        });
    }
});