import java.util.*;
import java.math.BigDecimal;
class Solution {
    public int solution(String[] lines) {
        int answer = 1;
        List<int[]> list = new ArrayList<>();
        for(int i=0;i<lines.length;i++){
            String line[] = lines[i].split(" ");
            String times[] = line[1].split(":");
            int h = Integer.parseInt(times[0])*60*60000;
            int m = Integer.parseInt(times[1])*60000;
            String ss[] = times[2].split("\\.");
            int s1 = Integer.parseInt(ss[0])*1000;
            int s2 = 0;
            if(ss.length>1)s2 = Integer.parseInt(ss[1]);
            int totalTimes = h+m+s1+s2;
            String ti[] = line[2].split("\\.");
            int s = 0;
            if(ti.length==1){
                String ti1[] = ti[0].split("s");
                s = Integer.parseInt(ti1[0])*1000;
            }else{
                String ti1[] = ti[1].split("s");
                s = Integer.parseInt(ti[0])*1000 + Integer.parseInt(ti1[0]);                
            }
            int startEnd[] = {totalTimes-s+1,totalTimes};
            list.add(startEnd);
        }

        for(int i=0;i<lines.length-1;i++){
            int startTime = list.get(i)[1];
            int endTime = startTime+999;
            int re = 1;
            for(int j=i+1;j<lines.length;j++){
                if(endTime>=list.get(j)[1] && (startTime<=list.get(j)[1] || startTime<=list.get(j)[0])) re++;
                else if(endTime>=list.get(j)[0] && endTime<=list.get(j)[1]) re++;
                else if(startTime>=list.get(j)[0] && startTime<=list.get(j)[1]) re++;
            }
            answer = Math.max(re,answer);
        }
        return answer;
    }
}