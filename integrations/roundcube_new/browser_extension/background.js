async function handleFileInfo(message, sendResponse) {
    const fileContent = message.data.filecontent;
    const { fileName, fileType, fileSize } = message.data;
    const fileMetadata = { fileName, fileType, fileSize };
    console.log("fileContent received on background.js:", fileContent);
    console.log("fileMetadata received on background.js:", fileMetadata);
    const formData = new FormData();
    const buffer = await fileContent.arrayBuffer();
    const blob = new blob([buffer], {
        type: fileContent.type,
    });

    formData.append(
        "fileMetadata",
        JSON.stringify(fileMetadata)
    )
    formData.append(
        "fileContent",
        blob,
        fileContent.name,
    )
    console.log("formData after appending:");
    console.log([...formData.entries()]);

    fetch("http:127.0.0.1:5000/get_file_info", {
        method = "POST",
        body = file,
    })
    .then((response) => {
        const result = response.json();
        console.log("the response from the fetch request received by background.js is: ", JSON.stringify(result, None, 4));
        sendResponse({
            success: true,
            data: result,
            policy_response: result,
        })
    })
    .catch((error) => {
        console.log("could not cotact DLP API:", error.stack);
        sendResponse({
            success: false,
            data:error.string(),
            policy_response: result,
        })
    })
    return ;
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.type !== "get_file_info") {
        return
    }
    if (message.type === "get_file_info") {
        handleFileInfo(message, sendResponse);
    }
    return true;
});