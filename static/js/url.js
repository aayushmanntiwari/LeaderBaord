function yourFunction(){
    var action_src = document.getElementsByName("pk")[0].value
    var your_form = document.getElementsByName("pk")[1].value
    console.log(action_src)
    var urlLink = window.location.href;
    urlLink = urlLink + action_src;

    action = urlLink;

}