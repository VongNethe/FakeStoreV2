from flask import app, render_template, request, redirect, url_for, flash, session
from app import app, db
from models.customer import Customer
import random

# -------------------------
# Register
# -------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        phone = request.form["phone"]
        address = request.form["address"]

        # Generate unique 6-digit customer ID
        customer_id = str(random.randint(100000, 999999))
        while Customer.query.filter_by(customer_id=customer_id).first():
            customer_id = str(random.randint(100000, 999999))

        new_customer = Customer(
            customer_id=customer_id,
            name=name,
            email=email,
            password=password,
            phone=phone,
            address=address
        )
        db.session.add(new_customer)
        db.session.commit()
        flash(f"Registered successfully! Your Customer ID: {customer_id}", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# -------------------------
# Login
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        password = request.form["password"]
        customer = Customer.query.filter_by(customer_id=customer_id, password=password).first()
        if customer:
            session["customer_id"] = customer.customer_id
            session["customer_name"] = customer.name
            return redirect(url_for("home"))
        else:
            flash("Invalid Customer ID or Password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

# -------------------------
# Logout
# -------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("login"))
