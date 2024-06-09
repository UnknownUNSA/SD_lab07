package es.rosamarfil.client;

import java.rmi.RemoteException;
import java.util.Arrays;
import javax.xml.rpc.ServiceException;
import es.rosamarfil.soap.SOAPI;
import es.rosamarfil.soap.SOAPImplServiceLocator;
import es.rosamarfil.model.User;

public class UserClient {
    public static void main(String[] args) {
        SOAPImplServiceLocator locator = new SOAPImplServiceLocator();

        try {
            SOAPI userService = locator.getSOAPImplPort();
            System.out.println("Lista de usuarios: \n" + Arrays.toString(userService.getUsers()));
            userService.addUser(new User("Pablo", "Ruiz"));
            System.out.println("Lista de usuarios: \n" + Arrays.toString(userService.getUsers()));
        } catch (ServiceException | RemoteException e) {
            e.printStackTrace();
        }
    }
}

