// console.log("DLP background service worker loaded");

// chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
//     if (message.type !== "get_file_info") {
//         return;
//     }

//     fetch("http://127.0.0.1:5000/get_file_info", {
//         method: "POST",

//         headers: {
//             "Content-Type": "application/json",
//         },

//         body: JSON.stringify(message.data),
//     })
//         .then((response) => response.json())
//         .then((result) => {
//             console.log("DLP RESULT:", result);

//             sendResponse({
//                 success: true,
//                 data: result,
//             });
//         })
//         .catch((error) => {
//             console.error("Could not contact DLP API:", error);

//             sendResponse({
//                 success: false,
//                 error: error.toString(),
//             });
//         });

//     return true;
// });

console.log("=====DLP gmail extension's background service loaded=====");

chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    if (message.type !== "get_file_info") {
        return;
    }
    if (message.type == "get_file_info") {
        console.log(message["data"]["fileContent"]);
        console.log(typeof message["data"]["fileContent"]);
        console.log(Object.keys(message["data"]["fileContent"]));

        const { fileName, fileType, fileSize } = message["data"];
        const metadata = { fileName, fileType, fileSize };
        console.log(
            `type of message.data.fileContent:`,
            message["data"]["fileContent"] instanceof File,
        );
        console.log(
            `type of message.data.fileContent:`,
            message["data"]["fileContent"] instanceof Blob,
        );
        console.log(`metadata :`);
        console.log(metadata);
        console.log(
            `file metadata received from content.js which is: ${JSON.stringify(message["data"], null, 4)}`,
        );
        const formData = new FormData();
        console.log(`formData at the time of initialization :`);
        console.log([...formData.entries()]);
        formData.append("fileMetadata", JSON.stringify(metadata));

        const file = message.data.fileContent; 
        const buffer = await file.arrayBuffer(); 
        const blob = new Blob([buffer], {
            type: file.type,
        });

        console.log("blob size:", blob.size);
        console.log("blob type:", blob.type);

        formData.append("fileContent", blob, file.name);
        console.log(`formData after appending data :`);
        console.log([...formData.entries()]);
        fetch("http://127.0.0.1:5000/get_file_info", {
            method: "POST",
            // headers: {
            //     "Content-Type": "application/json",
            // },
            body: formData,
        })
            .then(async (response) => {
                console.log("HTTP status:", response.status);
                const result = await response.text();
                console.log(`raw DLP result: ${JSON.stringify(result)}`);
                const resultJSON = JSON.parse(result);
                console.log(`DLP resultJSON: ${JSON.stringify(resultJSON)}`);
                // console.log(`DLP result: ${JSON.stringify(result)}`);
                sendResponse({
                    success: true,
                    data: result,
                });
            })
            .catch((error) => {
                console.log(`could not contact DLP API: ${error.stack}`);
                sendResponse({
                    success: false,
                    error: error.toString(),
                });
            });
    }
    return true;
});
