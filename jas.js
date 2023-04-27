function animation() {
  $(".app .click img").css("width", "180px");
  setTimeout(() => {
    $(".app .click img").css("width", "200px");
  }, 200);

}

function audio() {
  var audio = new Audio("muyu.mp3");
  audio.play();
}

function submit() {
  const if_share = document.getElementById("if_share").value;
  const text = document.getElementById("input").value;
  const title = document.getElementById("title").value;
  const connect = document.getElementById("contact").value;
  fetch('https://wsxar.cn/das/cyber', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ content: text, title: title, contact: connect, if_share: if_share })
  }).then(res => {
    if (res.status === 429) {
      alert("别nm发了");
      location.replace(location.href);
    }
    return res.json()
  }
  ).then(res => {
    if (res.message == '123') {
      alert("提交成功，请静候猫猫之神的审判");
      location.replace(location.href);
    }
    else if (res.message == '234') {
      alert("你注入nm呢！");
      location.replace(location.href);
    }
    else if (res.message == '456') {
      alert("别乱发包，好好写");
      location.replace(location.href);
    }
    else if (res.message == '345') {
      alert("咱正文多少得写点东西嘛");
      location.replace(location.href);
    }
    console.log(res);
  })
}

$("#submit").click(function (e) {
  console.log("sub");
  submit();
})

$(".app .click").click(function (e) {
  console.log("1223");
  animation();
  audio();
});
