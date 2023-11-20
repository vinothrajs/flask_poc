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
          if (i in loadOptions && isNotEmpty(loadOptions[i])) {
            args[i] = JSON.stringify(loadOptions[i]);
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
    { dataField: 'EffectiveFrom', caption: 'Effective From' },
    { dataField: 'EffectiveTill', caption: 'Effective Till' },
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
        showPageSizeSelector: true,
        allowedPageSizes: [2, 4, 6],
      },
      columns: columsdata,
    }).dxDataGrid('instance');
  });
  