package lab07;

import javax.xml.ws.Endpoint;

public class ProductServicePublisher {
    public static void main(String[] args) {

        Endpoint.publish("http://localhost:1516/WS/Lab07", new ProductSOAPService());
        System.out.println("Servicio SOAP publicado en http://localhost:1516/WS/Lab07");
    }
}

