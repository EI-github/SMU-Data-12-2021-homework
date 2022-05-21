$(document).ready(function() {
    console.log("Page Loaded");
    doWork();

    $("#selDataset").on("change", function() {
        makeDashboard()
    });
});

// global data because the RESPONSE is not changing
var global_data;

function doWork() {
    var url = "static/data/samples.json";
    requestAjax(url);
}

function makeDashboard() {
    let id = $("#selDataset").val();

    createMetadata(id);
    createBarChart(id);
    createBubbleChart(id);
    createGaugeChart(id);
}

function requestAjax(url) {
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            console.log(data);
            global_data = data;
            createDropdown();
            makeDashboard();
        },
        error: function(textStatus, errorThrown) {
            console.log("FAILED to get data");
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
}

function createDropdown() {
    var names = global_data.names;
    for (let i = 0; i < names.length; i++) {
        let name = names[i];
        let html = `<option>${name}</option>`;
        $("#selDataset").append(html);
    }
}

function createMetadata(id) {
    $("#sample-metadata").empty();
    let info = global_data.metadata.filter(x => x.id == id)[0];
    console.log(info);
    Object.entries(info).map(function(x) {
        let html = `<h6>${x[0]}: ${x[1]}</h6>`;
        $("#sample-metadata").append(html);
    });
}

function createBarChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        type: 'bar',
        x: sample.sample_values.slice(0, 10).reverse(),
        y: sample.otu_ids.map(x => `OTU ${x}`).slice(0, 10).reverse(),
        text: sample.otu_labels.slice(0, 10).reverse(),
        orientation: 'h'
    }

    var data1 = [trace1];
    var layout = {
        title: "Top 10 OTUs",
        xaxis: {
            title: "sample_values"
            },
        yaxis: {
            title: "otu_ids"
        }
    }

    Plotly.newPlot('bar', data1, layout);
}

function createBubbleChart(id) {
    let sample = global_data.samples.filter(x => x.id == id)[0];

    var trace1 = {
        x: sample.otu_ids,
        y: sample.sample_values,
        text: sample.otu_labels.slice(0, 10).reverse(),
        mode: 'markers',
        marker: {
            size: sample.sample_values,
            color: sample.otu_ids,
            colorscale: "RdBu"
        }
    }

    var data1 = [trace1];
    var layout = {
        "title": "OTU Samples",
        xaxis: {
            title: "OTU_ID"
            }
    }

    Plotly.newPlot('bubble', data1, layout);
}

function createGaugeChart(id) {
    let info = global_data.metadata.filter(x => x.id == id)[0];
    let avg = global_data["metadata"].map(x => x.wfreq).reduce((a, b) => a + b, 0) / global_data.metadata.length;

    var trace = {
        domain: { x: [0, 1], y: [0, 1] },
        value: info["wfreq"],
        title: { text: "Scrubs Per Week" },
        type: "indicator",
        mode: "gauge+number+delta",
        delta: { reference: avg.toFixed(2) },
        gauge: {
            axis: { range: [null, 10] },
            bar: { color: "rgb(7,54,66)" },
            steps: [
                { range: [0, 2], color: "rgb(192,242,243)" },
                { range: [2, 4], color: "rgb(129,219,219)" },
                { range: [4, 6], color: "rgb(72,203,197)" },
                { range: [6, 8], color: "rgb(30,156,153)" },
                { range: [8, 10], color: "rgb(0,112,108)" }
            ],
            threshold: {
                line: { color: "red", width: 4 },
                thickness: 0.75,
                value: 9.5
            }
        }
    };

    var data1 = [trace];

    var layout = {
        title: "Weekly Belly Button Wash Frequency"
    };
    Plotly.newPlot('gauge', data1, layout);
}