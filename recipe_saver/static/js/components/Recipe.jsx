import React from "react";
import Header from "./Header"

export default class Recipe extends React.Component {
    render() {
        return (
            <div className="container">
                <Header />
                <div className="recipe">
                    <p>recipe here</p>
                </div>
            </div>
        );
    }
}
