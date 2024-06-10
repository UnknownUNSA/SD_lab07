package es.rosamarfil.soap;

import java.util.List;
import javax.jws.WebService;
import es.rosamarfil.model.User;

@WebService(endpointInterface = "es.rosamarfil.soap.SOAPI")
public class SOAPImpl implements SOAPI {
	public List<User> getUsers() {
		return User.getUsers();
	}
	public void addUser(User user) {
		User.getUsers().add(user);
	}
}