document.getElementById("submitInput").addEventListener("click", inputUrl);

function inputUrl() {
    // get url values
    var url = document.getElementById("inputUrl").value;
    var infoDisplay = document.createElement("p");
    infoDisplay.textContent = url;
    
    // Hiển thị thông tin ngay dưới trường nhập liệu
    document.getElementById("display-info").appendChild(infoDisplay);
  }