function shortenUrl() {
            const originalUrl = document.getElementById('originalUrl').value;
            fetch('https://cl2u.ru/url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: originalUrl }),
            })
            .then(response => response.json())
            .then(data => {
                // Display the shortened URL to the user
                const shortenedUrl = data.short_link;
                const base64Image = "data:image/png;base64, " + data.qr_code;
                const imageElement = document.createElement("img");
                imageElement.src = base64Image;
                const imageContainer = document.getElementById("qrContainer");
                imageContainer.innerHTML = ""; // Clear previous content
                imageContainer.appendChild(imageElement);
                document.getElementById('shortenedUrl').href = shortenedUrl;
                document.getElementById('shortenedUrl').innerText = shortenedUrl.slice(8);
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('shortenedUrl').innerText = 'An error occurred while shortening the URL.';
            });
        }