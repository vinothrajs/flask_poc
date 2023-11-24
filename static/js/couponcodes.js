$(() => {
  function isNotEmpty(value) {
    return value !== undefined && value !== null && value !== '';
  }
  const store = new DevExpress.data.CustomStore({
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
        // console.log(i);
        // console.log(loadOptions[i]);
        if (i in loadOptions && isNotEmpty(loadOptions[i])) {
          args[i] = JSON.stringify(loadOptions[i]);
          console.log(args[i]);
        }
      });
      $.ajax({
        url: 'http://127.0.0.1:5000/get_couponcodes_json_paging',
        dataType: 'json',
        data: args,
        success(result) {
          console.log(result)
          deferred.resolve(result.coupons, {
            totalCount: result.totalCount
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
const columsdata = [
  { dataField: 'id', caption: 'ID' },
  { dataField: 'CouponCode', caption: 'Coupon Code' },
  { dataField: 'EffectiveFrom',dataType:'date',format:'yyyy-MM-dd', caption: 'Effective From' },
  { dataField: 'EffectiveTill',dataType:'date',format:'yyyy-MM-dd', caption: 'Effective Till' },
  { dataField: 'DiscountPercentage', caption: 'Discount Percentage' }
]
  $('#gridContainer').dxDataGrid({
    dataSource: store,
    showBorders: true,
    remoteOperations: true,
    paging: {
      pageSize: 2,
    },
    pager: {
      visible:true,
      showPageSizeSelector: true,
      allowedPageSizes: [2, 4, 6],
    },
    sorting:{
      mode:'multiple'
    },
    filterRow: { visible: true },
    columns: columsdata,
  }).dxDataGrid('instance');
});
