import java.util.Scanner;

public class media {
    public static void main(String[] args) {
        int SomaNumerosPares = 0;
        int SomaNumerosImpares = 0;
        int quantidadeNumerosPares = 0;
        int quantidadeNumerosImpares = 0;
        int mediaPares = 0;
        int mediaImpares = 0;

        System.out.println("Digite os numeros separados por espaco: ");
        Scanner scan = new Scanner(System.in);
        String numeros = scan.nextLine();
        String[] numerosSeparados = numeros.split(" ");

        for (int i = 0; i < numerosSeparados.length; i++) {
            if (Integer.parseInt(numerosSeparados[i]) % 2 == 0) {
                SomaNumerosPares += Integer.parseInt(numerosSeparados[i]);
                quantidadeNumerosPares++;
            } else {
                SomaNumerosImpares += Integer.parseInt(numerosSeparados[i]);
                quantidadeNumerosImpares++;
            }
        }
        mediaPares = SomaNumerosPares / quantidadeNumerosPares;
        mediaImpares = SomaNumerosImpares / quantidadeNumerosImpares;
        System.out.println("Media dos numeros pares: " + mediaPares);
        System.out.println("Mèdia dos numeros impares: " + mediaImpares);
        scan.close();
    }

}