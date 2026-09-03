console.log("=====DLP service worker loaded=====");

async function handleFileInfo(message, sendResponse) {
    console.log(
        `the message received by background.js is: ${JSON.stringify(message, null, 4)}`,
    );
    const fileContent = message.data.fileContent;
    console.log("message.data:", message.data);
    const { fileName, fileType, fileSize } = message.data;
    const fileMetadata = { fileName, fileType, fileSize };
    console.log("fileContent received on background.js:", fileContent);
    console.log("fileMetadata received on background.js:", fileMetadata);
    const formData = new FormData();
    const buffer = await fileContent.arrayBuffer();
    const blob = new Blob([buffer], {
        type: fileContent.type,
    });

    formData.append("fileMetadata", JSON.stringify(fileMetadata));
    formData.append("fileContent", blob, fileContent.name);
    console.log("formData after appending:");
    console.log([...formData.entries()]);

    fetch("http:127.0.0.1:5000/get_file_info", {
        method: "POST",
        body: formData,
    })
        .then(async (response) => {
            // const fetchResponse = await response.text();
            // console.log(
            //     "the fetchResponse from the fetch request in background.js is:",
            //     JSON.stringify(fetchResponse),
            // );
            // const result = await JSON.parse(fetchResponse);
            const result = await response.json();
            console.log(
                "the response from the fetch request received by background.js is: ",
                JSON.stringify(result, null, 4),
            );
            // console.log(
            //     "the response from the fetch request received by background.js is: ",
            //     JSON.stringify(result),
            // );
            sendResponse({
                success: true,
                data: result,
                policy_response: result,
            });
        })
        .catch((error) => {
            console.log("could not cotact DLP API:", error.stack);
            sendResponse({
                success: false,
                data: error.toString(),
                policy_response: result,
            });
        });
    return;
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type !== "get_file_info") {
        return;
    }
    if (message.type === "get_file_info") {
        handleFileInfo(message, sendResponse);
    }
    return true;
});
