function test2(liex,liey){        
$(function () {
    $('#WCDF').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'CDF of Waiting Time'
        },
        xAxis: {
             tickInterval:500,
             categories: liex,
	     title:{
		text:'ms',
		align:'high'
             },
	     labels:{
		enabled:false
	     }
        },
        yAxis: {
            title: {
                text: 'CDF(%)'
            },
            max:1,
            min:0,
            tickInterval:0.25
        },
	legend:{
	    enabled:false
        },
	credits:{
	    enabled:false
	},
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<td style="padding:0"><b>{point.y:.3f}</b></td></tr>',
            shared: true,
            useHTML: true
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
