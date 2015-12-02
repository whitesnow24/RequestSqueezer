function test1(liex,liey){       
 $(function () {
    $('#SCDF').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'CDF of Response Time'
        },
        xAxis: {
            title:{
                text:'ms',
		align:'high'
            },
 	    tickInterval:500,
	    categories:liex,
	    labels:{
		enabled:false
	    }
        },
        yAxis: {
            title: {
                text: 'CDF(%)',
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
