///////////////////////////////
// Question 10: Bank Account //
///////////////////////////////

// It should have an interest rate where interest has to be paid to the bank as and 
// when required, and a credit limit which is the maximum limit on the amount owed to the 
// bank (assuming the amount will not exceed the limit after paying interest). We should 
// be able to transfer money among these various types of accounts.

//Subclass
// class LoanAcct extends BankAcct
// {
// 	protected double _rate;
// 	protected double _limit;
    
// 	public LoanAcct(int aNum, double bal, double rate, double limit) {
//         // initialize attributes with user provided values
//         super( aNum, bal );
//         _rate = rate;
//         _limit = limit;
//         _balance = bal;
//         _acctNum = aNum;

// 	}

// 	//New method in subclass
// 	public void payInterest() {
// 		_balance -= _rate;
// 	}

// 	//Method Overriding
// 	public boolean withdraw( double amount ) {
//         if (_balance-amount < -_limit)
//             return false;
//         _balance -= amount;
//             return true;
// 	}

// 	public void deposit( double amount ) {
//         _balance += amount;
// 	}
// }

// public boolean transfer (BankAcct fromAcct, BankAcct toAcct, double amount) {
// 	if (fromAcct.withdraw(amount)) {
// 		toAcct.deposit(amount);
// 		return true;
// 	}
// 	return false;
// }

///////////////////////////////////////
// Question 11: Complex Number class //
///////////////////////////////////////

public interface Complex { 
	public double realpart ( );        // returns this.real
	public double imagpart( );         // returns this.imag
	public double angle ( );           // returns this.angle
	public double magnitude      ( );  // returns this.mag
	public void  add   (Complex c);    // this = this + c
	public void  minus (Complex c);    // this = this - c
	public void  times (Complex c);    // this = this * c
	public void  divides(Complex c);
}

class ComplexCart implements Complex { 
	private double real;
	private double imag;
	// CONSTRUCTORS 
	public ComplexCart (double r, double i) { real = r; imag = i; }

	// ACCESSORS
	public double realpart ()  {  return this.real; }
	public double imagpart ()  { return this.imag; }
	public double magnitude () { return Math.sqrt(real * real + imag * imag); }  
	public double angle ()  {
		if (real != 0) {
			if (real < 0 ) return (Math.PI + Math.atan(imag/real));
			return Math.atan(imag / real);
		}
		else if (imag == 0) return 0;
		else if (imag > 0) return Math.PI/2; 
		else return -Math.PI/2; 
	}

	// MUTATORS
	public void add (Complex c)  {
		this.real += c.realpart(); 
		this.imag += c.imagpart(); 
	}

	public void minus (Complex c)   { 
		this.real -= c.realpart(); 
		this.imag -= c.imagpart(); 
	}

	public void times (Complex c)   { 
		double tempReal=real*c.realpart() - imag*c.imagpart();    
		imag = real * c.imagpart() + imag * c.realpart(); 
		real = tempReal;
	}

	public void divides (Complex c) {
        double tempReal = real;
		real = (real * c.realpart() + imag * c.imagpart()) / 
                        (Math.pow(c.realpart(), 2) + Math.pow(c.imagpart(), 2));
        imag = (imag * c.realpart() - tempReal * c.imagpart()) / 
                            (Math.pow(c.realpart(), 2) + Math.pow(c.imagpart(), 2));
    }

	// for printing... 
	public String toString() {
		if ( imag == 0 ) return ( realpart() + "");
		else if ( imag < 0 ) 
			return ( real + "" + imag + "i");
		else 
			return ( real + "+" + imag + "i");
	}
}

class ComplexPolar implements Complex {
	private double mag;   // magnitude
	private double ang;   // angle
	// CONSTRUCTORS
	ComplexPolar (double m, double r) { mag = m; ang = r; } 

	// ACCESSORS
	public double realpart ()  { return mag * Math.cos(ang); }
	public double imagpart ()  { return mag * Math.sin(ang); }   
	public double magnitude () { return mag; }
	public double angle ()     { return ang; }

	// MUTATORS
	public void add (Complex c)   {     // this = this + c
		double real =  realpart() + c.realpart();
		double imag =  imagpart() + c.imagpart(); 
		mag = Math.sqrt(real*real + imag*imag);
		if (real != 0) { 
			if (real < 0) ang = (Math.PI + Math.atan(imag/real));
			else ang = Math.atan(imag/real);
		}
		else if (imag == 0) ang = 0;
		else if(imag > 0) ang = Math.PI/2;
		else ang = -Math.PI/2;
	}

	public void minus (Complex c)   {     // this = this - c
		double real =  mag * Math.cos(ang) - c.realpart(); 
		double imag =  mag * Math.sin(ang) - c.imagpart();
		mag = Math.sqrt(real*real + imag*imag);
		if (real != 0) { 
			if (real < 0) ang = (Math.PI + Math.atan(imag/real));
			else ang = Math.atan(imag/real);
		}
		else if (imag == 0) ang = 0;
		else if(imag > 0) ang = Math.PI/2;
		else ang = -Math.PI/2;
	}

	public void times (Complex c)  {   // this = this * c
		mag *= c.magnitude(); 
		ang += c.angle();
		ang = ang % (2*Math.PI); // maintain ang within 2*pi 
	}

	public void divides (Complex c) {
		mag /= c.magnitude();
        ang -= c.angle();
	}

	public String toString() {
		if ( imagpart() == 0 ) return ( this.realpart() + "");
		else if ( imagpart() < 0 ) 
			return ( realpart() + "" + imagpart() + "i");
		else 
			return ( realpart() + "+" + imagpart() + "i");
	}
}