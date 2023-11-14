var prod = (function() {
   function _saveData() {
        const data = {
            name :"Raj",
            age :"20"
        }
        document.getElementById("showoutput").innerHTML =
        data.name + " is " + data.age + " years old.";
   }
   function _getdata() {
        fetch('https://jsonplaceholder.typicode.com/users')
        .then(response => response.json())
        .then(json => createList(json))
   }
   function createList(data) {
    var features = document.getElementById('foo');
    var ul = document.createElement('ul');
    for (var i = 0; i < data.length; ++i) {
      var li = document.createElement('li');
      ul.appendChild(li);
      li.innerHTML = data[i].name;
      li = document.createElement('li');
      ul.appendChild(li);
      li.innerHTML = data[i].phone;
    }
    features.appendChild(ul);
  }
    return {
        saveData: _saveData,
        getdata: _getdata
    }
})();
