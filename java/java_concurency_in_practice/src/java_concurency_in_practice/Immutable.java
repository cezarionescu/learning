package java_concurency_in_practice;

public class Immutable {
	private final int counter;
	
	public Immutable (int counter) {
		this.counter = counter;
	}
	
	public int get() {
		return counter;
	}
}
