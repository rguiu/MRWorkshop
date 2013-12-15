// from: http://dimplejs.org/examples_viewer.html?id=lines_horizontal_stacked
var svg_all = dimple.newSvg('#gchart', 975, 275);

d3.csv("data/monthly_average.csv", function (data) {
      var myChart = new dimple.chart(svg_all, data);
      myChart.setBounds(60, 30, 920, 225);
      var x = myChart.addCategoryAxis("x", "month");
      x.addOrderRule("month");
      myChart.addMeasureAxis("y", "average");
      myChart.addSeries("year", dimple.plot.line);
      myChart.addLegend(60, 10, 900, 20, "right");
      myChart.draw();
});
