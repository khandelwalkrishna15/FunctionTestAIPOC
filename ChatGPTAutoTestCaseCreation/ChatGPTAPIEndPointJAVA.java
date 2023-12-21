import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.concurrent.CompletableFuture;

public class ChatGPTApiClient {

    public static void main(String[] args) {
        // Set your API key here
        String apiKey = "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";

        // Set the API endpoint URL
        String apiUrl = "https://api.openai.com/v1/chat/completions";

        // Input text to send to the API
        String prompt = "Who is India PM";

        // Create an HttpClient
        HttpClient httpClient = HttpClient.newBuilder().build();

        // Create a JSON request payload
        String jsonPayload = "{\"prompt\": \"" + prompt + "\", \"max_tokens\": 50}";

        // Create an HTTP request
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(apiUrl))
                .POST(HttpRequest.BodyPublishers.ofString(jsonPayload))
                .header("Authorization", "Bearer " + apiKey)
                .header("Content-Type", "application/json")
                .build();

        // Send the HTTP request and handle the response asynchronously
        CompletableFuture<HttpResponse<String>> responseFuture = httpClient.sendAsync(request, HttpResponse.BodyHandlers.ofString());

        // Handle the response when it's available
        responseFuture.thenAccept(response -> {
            int statusCode = response.statusCode();
            String responseBody = response.body();

            if (statusCode == 200) {
                System.out.println("API Response:\n" + responseBody);
            } else {
                System.err.println("Error: HTTP " + statusCode + "\n" + responseBody);
            }
        }).exceptionally(e -> {
            System.err.println("Request failed: " + e.getMessage());
            return null;
        });

        // Wait for the response asynchronously (you can also use CompletableFuture.join())
        responseFuture.join();
    }
}
