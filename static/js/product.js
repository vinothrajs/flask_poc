'use strict';
 
// var prod = (function() {
//   function _saveData() {
//        const data = {
//            name :"Raj",
//            age :"20"
//        }
//        document.getElementById("showoutput").innerHTML =
//        data.name + " is " + data.age + " years old.";
//   }
//   function _getdata() {
//        fetch('https://jsonplaceholder.typicode.com/users')
//        .then(response => response.json())
//        .then(json => createList(json))
//   }
//   function createList(data) {
//    var features = document.getElementById('foo');
//    var ul = document.createElement('ul');
//    for (var i = 0; i < data.length; ++i) {
//      var li = document.createElement('li');
//      ul.appendChild(li);
//      li.innerHTML = data[i].name;
//      li = document.createElement('li');
//      ul.appendChild(li);
//      li.innerHTML = data[i].phone;
//    }
//    features.appendChild(ul);
//  }
//    return {
//        saveData: _saveData,
//        getdata: _getdata
//    }
// })();


 var ProductManager = {
   basePath: function () { return 'https://jsonplaceholder.typicode.com'; },
   getdata: function () {
      $.ajax({
          url: this.basePath() + '/users',
          dataType: 'json',
          cache: false,
          success: function (data) {
            ProductManager.createList(data);
          }
      });
  },
  createList : function (data){
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
  },
  showdata : function (){
    const data = {
      name :"Raj",
      age :"20"
  }
  document.getElementById("showoutput").innerHTML = data.name + " is " + data.age + " years old.";
  }
}

// Over ride a funcation 
class Human {
  constructor(weapon) {
   this.weapon = weapon;
   this.health = 100;
  }
  receiveDamage() {
   this.health = this.health - 100;
  }
 }
 class Wizard extends Human {
  receiveDamage() {
    super.receiveDamage(); //calling parent class method via keyword 'super'
   this.health = this.health - 5;

  }
 }
 const wizard = new Wizard("staff");
 console.log(wizard.health);
 wizard.receiveDamage();
 console.log(wizard.health);

//documet ready
 $(document).ready(function () {

  $('#newbutton').click(function (e) {
    e.preventDefault();
    alert("newbutton clieck")
  });
  
 });


 $(() => {
  function isNotEmpty(value) {
    return value !== undefined && value !== null && value !== '';
  }
  const store = new DevExpress.data.CustomStore({
    key: 'OrderNumber',
    load(loadOptions) {
      const deferred = $.Deferred();
      const args = {};

      [
        'skip',
        'take',
        'requireTotalCount',
        'requireGroupCount',
        'sort',
        'filter',
        'totalSummary',
        'group',
        'groupSummary',
      ].forEach((i) => {
        if (i in loadOptions && isNotEmpty(loadOptions[i])) {
          args[i] = JSON.stringify(loadOptions[i]);
        }
      });
      $.ajax({
        url: 'https://js.devexpress.com/Demos/WidgetsGalleryDataService/api/orders',
        dataType: 'json',
        data: args,
        success(result) {
          console.log(result)
          deferred.resolve(result.data, {
            totalCount: result.totalCount,
            summary: result.summary,
            groupCount: result.groupCount,
          });
        },
        error() {
          deferred.reject('Data Loading Error');
        },
        timeout: 5000,
      });
     

      return deferred.promise();
    },
  });
const columsdata = [{
  dataField: 'OrderNumber',
  dataType: 'number',
}, {
  dataField: 'OrderDate',
  dataType: 'date',
}, {
  dataField: 'StoreCity',
  dataType: 'string',
}, {
  dataField: 'StoreState',
  dataType: 'string',
}, {
  dataField: 'Employee',
  dataType: 'string',
}, {
  dataField: 'SaleAmount',
  dataType: 'number',
  format: 'currency',
}]
  $('#gridContainer').dxDataGrid({
    dataSource: store,
    showBorders: true,
    remoteOperations: true,
    paging: {
      pageSize: 10,
    },
    pager: {
      showPageSizeSelector: true,
      allowedPageSizes: [10, 50, 100],
    },
    columns: columsdata,
  }).dxDataGrid('instance');
});
