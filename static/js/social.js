function commentReplyToggle(parent_id){
    const row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

function showNotifications(){
    const container = document.getElementById('notification-container');

    if (container.classList.contains('d-none')){
        container.classList.remove('d-none');
    }
    else {
        container.classList.add('d-none');
    }
}

function shareToggle(parent_id){
    const row = document.getElementById(parent_id);

    if (row.classList.contains('d-none')) {
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

function formatTags(){
    const elements = document.getElementByClassname('body');
    for (let i=0; i= elements.length; i++){
        let bodytext = elements[i].children[0].innerText;

        let words = bodyText.split(" ");

        for (let j=0; j < words.length; j++){
            if (words[j][0] == "#"){
                let replacedText = bodyText.replace(#([^\\s]*),g, "<a href="#">${words[j]}</a>");
                elements[i].innerHTML = replacedText
            }
        }

    }
}

formatTags()