class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int low = 0;int high = height.length-1;
        int maxarea = 0; int a = 0;
        while (low < high) {
            if (height[low] > height[high]) {
                a = height[high] * (high-low);
                high--;
            } else {
                a = height[low] * (high-low);
                low++;
            }
            if (maxarea < a) maxarea = a;
        }
        return maxarea;
    }
}
