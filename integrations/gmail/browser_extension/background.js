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

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type !== "get_file_info") {
        return;
    }
    if (message.type == "get_file_info") {
        fetch("http://127.0.0.1:5000/get_file_info", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(message.data),
        })
            .then(async (response) => {
                const result = await response.json();
                console.log(`DLP result: ${JSON.stringify(result)}`);
                sendResponse({
                    success: true,
                    data: result,
                });
            })
            .catch((error) => {
                console.log(`could not contact DLP API: ${error}`);
                sendResponse({
                    success: false,
                    error: error.toString(),
                });
            });
        // fetch("http://127.0.01:5000/")
    }
    return true;
});
