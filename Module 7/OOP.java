class BuildingBlueprint{
    static int num_buildings = 0;

    int num_stories;
    int num_apts;
    double occupancy;
    boolean is_full;

    BuildingBlueprint(int ns, int na, double o){
        num_stories = ns;
        num_apts = na;
        occupancy = o;
        is_full = occupancy == 1.0;
    }

    BuildingBlueprint(){
        num_stories = 10;
        num_apts = 20;
        occupancy = 1.0;
        is_full = occupancy == 1.0;
    }

    public void update_occupancy(double o){
        occupancy = o;
        is_full = occupancy == 1.0;
    }
}

public class OOP {
    public static void main(String[] args) {
        BuildingBlueprint building_one = new BuildingBlueprint(50, 250, 0.7);
        BuildingBlueprint building_two = new BuildingBlueprint();

        System.out.println("Building one has " + building_one.num_stories + " stories");
        System.out.println("Building two has " + building_two.num_stories + " stories");

        System.out.print("Building one is ");
        if(building_one.is_full){
            System.out.println("full.");
        }
        else{
            System.out.println("is not full.");
        }

        building_one.update_occupancy(1.0);

        System.out.print("Building one is ");
        if(building_one.is_full){
            System.out.println("full.");
        }
        else{
            System.out.println("is not full.");
        }
        
    }
}
