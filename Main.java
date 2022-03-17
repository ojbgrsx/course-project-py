import java.util.*;

public class Main {
    public static void main(String[] args) {
        run();
    }

    public static void clients_account() {
        int i = 0;
        if (i == 0) {
            Scanner scanCL = new Scanner(System.in);
            String selectedNum = "";
            while (!selectedNum.equals("8")) {
                System.out.println();
                System.out.println("1) Show my credit records");
                System.out.println("2) Show my funds:");
                System.out.println("3) Buy currency:");
                System.out.println("4) Make a money transfer on ID:");
                System.out.println("5) Transactions with my participation:");
                System.out.println("6) Close the loan:");
                System.out.println("7) Back to the main menu");
                System.out.println("8) Exit");
                System.out.print("Menu selection >>> ");
                selectedNum = scanCL.nextLine();
                System.out.println();
                switch (selectedNum) {
                    case "1":
                        break;
                    case "2":
                        break;
                    case "3":
                        break;
                    case "4":
                        break;
                    case "5":
                        break;
                    case "6":
                        break;
                    case "7":
                        run();
                        break;
                    case "8":
                        System.out.println("\nThe program is over, we look forward to your return\n");
                        break;
                }
            }
            scanCL.close();
        }
    }

    public static ArrayList<String> registration() {
        Scanner scanREG = new Scanner(System.in);
        // int a = scanREG.nextInt();
        ArrayList<String> list = new ArrayList<>();
        System.out.print("Enter username >>> ");
        String name = scanREG.nextLine();
        System.out.print("Enter password >>> ");
        String password = scanREG.nextLine();
        list.add(name);
        list.add(password);
        scanREG.close();
        return list;
    }

    private static void worker_account() {
        int i = 0;

        if (i == 0) {
            Scanner scanWOR = new Scanner(System.in);
            String selectedNum = "";
            while (!selectedNum.equals("9")) {
                System.out.println();
                System.out.println("Please, dial the number to run the program, if you are finished, dial 9:");
                System.out.println("1) Show the list of clients");
                System.out.println("2) Find and select the client:");
                System.out.println("3) Show the name of the client who took the maximum credit");
                System.out.println("4) Show the name of the client who took the minimum credit");
                System.out.println("5) Set a new amount for conversion:");
                System.out.println("6) Make a money transfer:");
                System.out.println("7) Calculate the amount of transfers:");
                System.out.println("8) Back to the main menu");
                System.out.println("9) Exit");
                System.out.print("Menu selection >>> ");
                selectedNum = scanWOR.nextLine();
                System.out.println();
                switch (selectedNum) {
                    case "1":
                        break;
                    case "2":
                        break;
                    case "3":
                        break;
                    case "4":
                        break;
                    case "5":
                        break;
                    case "6":
                        break;
                    case "7":
                        break;
                    case "8":
                        run();
                        break;
                    case "9":
                        System.out.println("The program is over, we look forward to your return");
                        break;
                }
            }
            i++;
            scanWOR.close();
        }
    }

    public static void run() {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> workers_data = new ArrayList<String>(Arrays.asList("akylbek", "bolsunbekov"));
        ArrayList<String> clients_data = new ArrayList<String>(Arrays.asList("azat", "izambaev"));
        ArrayList<ArrayList<String>> workers = new ArrayList<ArrayList<String>>();
        ArrayList<ArrayList<String>> clients = new ArrayList<ArrayList<String>>();
        workers.add(workers_data);
        clients.add(clients_data);
        System.out.println("\nYou are welcome Dear User !!!".toUpperCase());
        System.out.println("\n1) Sign in as WORKER\n2) Sign in as CLIENT\n3) Sign up\n4) Exit");
        System.out.print("Select >>> ");
        int account_type = scan.nextInt();
        String qwerty = scan.nextLine();
        if (account_type == 1) {
            int a, b;
            a = b = 0;
            for (int q = 3; q > 0; q--) {
                System.out.print("Enter your username >>> ");
                String username = scan.nextLine().toLowerCase();
                for (int count = 0; count < workers.size(); count++) {
                    if (workers.get(count).get(0).equals(username)) {
                        for (int i = 3; i > 0; i--) {
                            System.out.print("Enter your password >>> ");
                            String password = scan.nextLine().toLowerCase();
                            if (password.equals(workers.get(count).get(1))) {
                                System.out.println("Correct Password !!!");
                                worker_account();
                                a++;
                                break;
                            } else {
                                System.out.println("Wrong password !!!");
                                if (i != 1) {
                                    System.out.println(String.format("%d attempts left", i - 1));
                                }
                                b++;
                            }
                        }
                        break;
                    }
                }
                if (a == 1 || b == 3) {
                    break;
                } else {
                    System.out.println("Wrong username !!!");
                    if (q != 1) {
                        System.out.println(String.format("%d attempts left", q - 1));
                    }
                }
            }
        } else if (account_type == 2) {
            int a, b;
            a = b = 0;
            for (int q = 3; q > 0; q--) {
                System.out.print("Enter your username >>> ");
                String username = scan.nextLine().toLowerCase();
                for (int count = 0; count < clients.size(); count++) {
                    if (clients.get(count).get(0).equals(username)) {
                        for (int i = 3; i > 0; i--) {
                            System.out.print("Enter your password >>> ");
                            String password = scan.nextLine().toLowerCase();
                            if (password.equals(clients.get(count).get(1))) {
                                System.out.println("Correct Password !!!");
                                clients_account();
                                a++;
                                break;
                            } else {
                                System.out.println("Wrong password !!!");
                                if (i != 1) {
                                    System.out.println(String.format("%d attempts left", i - 1));
                                }
                                b++;
                            }
                        }
                        break;
                    }
                }
                if (a == 1 || b == 3) {
                    break;
                } else {
                    System.out.println("Wrong username !!!");
                    if (q != 1) {
                        System.out.println(String.format("%d attempts left", q - 1));
                    }
                }
            }
        } else if (account_type == 3) {
            System.out.println("\n1)As WORKER\n2)As CLIENT\n");
            int qr = scan.nextInt();
            ArrayList<String> list = registration();
            if (qr == 1) {
                workers.add(list);
                System.out.println("You've successfully signed up as worker !!!");
            } else if (qr == 2) {
                clients.add(list);
                System.out.println("You've successfully signed up as client !!!");
            }
        } else {
            System.out.println("\nThe program is over, we look forward to your return");
        }
        scan.close();
    }

}