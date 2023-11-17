  // Function to fetch data from the Flask endpoint

//   function fetchData() {
//     $.ajax({
//         url: 'http://127.0.0.1:5000/get_couponcodes_json',
//         type: 'GET',
//         dataType: 'json',
//         // headers: {
//         //     'Authorization': 'Bearer your_secret_token'
//         // },
//         success: function (data) {
//             // Check if the request was successful
//             if (data && data.coupons) {
//                 // Bind data to the DevExpress grid
//                 bindDataToGrid(data.coupons);
//             } else {
//                 console.error('Error:', data.error);
//             }
//         },
//         error: function (error) {
//             console.error('Error:', error);
//         }
//     });
// }
  function isNotEmpty(value) {
    return value !== undefined && value !== null && value !== '';
  }
  const fetchDatastore = new DevExpress.data.CustomStore({
    key: 'id',
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
        url: 'http://127.0.0.1:5000/get_couponcodes_json',
        type: 'GET',
        dataType: 'json',
        data: args,
        success(result) {
          console.log(result)
          deferred.resolve(result.coupons, 
            // {
            //     totalCount: result.totalCount,
            //     summary: result.summary,
            //     groupCount: result.groupCount,
            // }
          );
        },
        error() {
          deferred.reject('Data Loading Error');
        },
        timeout: 5000,
      });

      return deferred.promise();
    },
  });
 

// Function to bind data to DevExpress grid
function bindDataToGrid() {
    $("#gridContainer").dxDataGrid({
        dataSource: fetchDatastore,
        columns: [
            { dataField: 'id', caption: 'ID' },
            { dataField: 'CouponCode', caption: 'Coupon Code' },
            { dataField: 'EffectiveFrom', caption: 'Effective From' },
            { dataField: 'EffectiveTill', caption: 'Effective Till' },
            { dataField: 'DiscountPercentage', caption: 'Discount Percentage' }
        ],
        showBorders: true,
        paging: {
            pageSize: 10
        },
        pager: {
            showPageSizeSelector: true,
            allowedPageSizes: [5, 10, 20],
            showInfo: true
        }
    });
}

// Call the fetchData function when the page loads
$(document).ready(function () {
    bindDataToGrid();
});