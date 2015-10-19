package com.example;

import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.Client;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.transport.InetSocketTransportAddress;

import static spark.Spark.*;

public class Main {


    private static Client client = new TransportClient()
                            .addTransportAddress(new InetSocketTransportAddress("localhost", 9300));

    public static void main(String[] args) {
        get("/stats", (req, res) -> {
                    SearchResponse response = client
                        .prepareSearch("nfl")
                        .setSize(50)
                        .execute()
                        .actionGet();
                    return  response.toString();
                }
        );
    }
}