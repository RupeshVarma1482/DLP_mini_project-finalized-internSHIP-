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

document.addEventListener("change", async(event) => {
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
        console.log(`file:`);
        console.log(file);

        // fetch("http:127.0.0.1:5000/get_file_info", {
        //     method: "POST",
        //     headers: {
        //         "Content-Type": "application/octet-stream"
        //     },
        //     body: file
        // })
        // .then((response) => {
        //     console.log(`response obtained`);
        // })
        // .catch((error) => {
        //     console.log(`error is: ${error}`);
        // })

        const buffer = await file.arrayBuffer()
        console.log(`fileByteLength : ${buffer.byteLength}`);

        const data = {
            "fileName" : file.name,
            "fileType" : file.type,
            "fileSize" : file.size,
            "fileContent" : buffer
        };
        chrome.runtime.sendMessage({
            "type" : "get_file_info",
            "data" : data
        });
    }
});