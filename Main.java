package com.company;

public class Main {

    public static void main(String[] args) {

        final int TIMES = 1000;
        Singletone arr[] = new Singletone[TIMES];
        for (int i=0; i<TIMES; i++){
            arr[i] = Singletone.getInstance();
        }
    System.out.println(Singletone.counter);
    }
}
class Singletone{
    public static int counter = 0;
    private static Singletone instance;
    private Singletone(){
        counter++;
    }

    public static Singletone getInstance(){
    if(instance == null){
        instance = new Singletone();
    }
        return instance;
    }
}
