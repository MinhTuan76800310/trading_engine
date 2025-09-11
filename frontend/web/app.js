const chart = LightweightCharts.createChart(document.getElementById('chart'), {
    width: window.innerWidth,
    height: 600,
    timeScale: { timeVisible: true, secondsVisible: false },
});

const candlestickSeries = chart.addCandlestickSeries({
    upColor: '#26a69a',
    downColor: '#ef5350',
    borderVisible: false,
    wickUpColor: '#26a69a',
    wickDownColor: '#ef5350',
});

function connectWebSocket() {
    const ws = new WebSocket('ws://localhost:8765');
    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        const candle = {
            time: data.timestamp / 1000, // Convert ms to seconds
            open: data.open,
            high: data.high,
            low: data.low,
            close: data.close,
        };
        candlestickSeries.update(candle);
    };
    ws.onopen = () => {
        console.log('Connected to WebSocket relay');
    };
    ws.onerror = (error) => {
        console.error('WebSocket error:', error);
    };
    ws.onclose = () => {
        console.log('WebSocket closed, reconnecting...');
        setTimeout(connectWebSocket, 5000);
    };
    return ws;
}

let ws = connectWebSocket();

window.addEventListener('resize', () => {
    chart.resize(window.innerWidth, 600);
});