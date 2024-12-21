async function fetchStatus() {
    try {

        const endpoints = [
            { id: 'contoh-jarak', url: '/get_status/contoh/' },
            { id: 'kelompok_1-jarak', url: '/get_status/kelompok_1/' },
            { id: 'kelompok_2-jarak', url: '/get_status/kelompok_2/' },
            { id: 'kelompok_3-jarak', url: '/get_status/kelompok_3/' },
            { id: 'kelompok_4-jarak', url: '/get_status/kelompok_4/' },
            { id: 'kelompok_5-jarak', url: '/get_status/kelompok_5/' },
            { id: 'kelompok_6-jarak', url: '/get_status/kelompok_6/' },
        ];

        const fetches = endpoints.map(async (endpoint) => {
            const response = await fetch(endpoint.url);
            if (response.ok) {
                const data = await response.json();
                document.getElementById(endpoint.id).textContent = data.Jarak + " cm"|| '0.0';
            } else {
                console.error(`Failed to fetch status from ${endpoint.url}:`, response.status);
            }
        });

        await Promise.all(fetches);
    } catch (error) {
        console.error('Error fetching status:', error);
    }
}

setInterval(fetchStatus, 1000);
window.onload = fetchStatus;
