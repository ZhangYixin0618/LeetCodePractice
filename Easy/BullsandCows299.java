import java.util.HashMap;

public class BullsandCows299 {


    public static String getHint(String secret, String guess) {
        int bull = 0;
        int cow = 0;
        char[] secret_sb = secret.toCharArray();
        char[] guess_sb = guess.toCharArray();

        HashMap<Character, Integer> nums_map = new HashMap<>();

        for (int i = 0; i < secret_sb.length; i++) {
            if (secret_sb[i] == guess_sb[i]) {
                secret_sb[i] = 'A';
                guess_sb[i] = 'A';
                bull++;
            } else {
                if (nums_map.containsKey(secret_sb[i])) {
                    nums_map.put(secret_sb[i], nums_map.get(secret_sb[i]) + 1);
                } else {
                    nums_map.put(secret_sb[i], 1);
                }
            }
        }

        for (int i = 0; i < guess_sb.length; i++) {
            if (guess_sb[i] != 'A') {
                if (nums_map.containsKey(guess_sb[i])) {
                    if (nums_map.get(guess_sb[i]) > 0) {
                        cow += 1;
                        nums_map.put(guess_sb[i], nums_map.get(guess_sb[i]) - 1);
                    }
                }
            }
        }
        return bull + "A" + cow + "B";
    }


    public static void main(String[] args) {
        String a = getHint("011", "110");
        System.out.println(a);


    }


}
