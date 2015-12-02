function test4(liex,liey){        
$(function () {
    $('#WHist').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Histogram of Waiting Time'
        },
        xAxis: {
	     tickInterval:500,
             categories:liex,
	     title:{
		text:'ms',
		align:'high'
             }
        },
        yAxis: {
            max: 0.25,
            min: 0,
            title: {
                text: 'percent(%)'
            }
        },
	legend:{
	    enabled:false
	},
	credits:{
	    enabled:false
	},
        tooltip: {
            pointFormat: '<td style="padding:0"><b>{point.y:.3f}</b></td></tr>',
            shared: false,
            useHTML: false
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            data: liey
        }]
    });
});
}
