package rosamarfil.es;
import javax.xml.ws.Endpoint;
import es.rosamarfil.soap.SOAPImpl;
public class PublishServices {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Endpoint.publish("http://localhost:1516/WS/Users", new SOAPImpl());
	}

}
