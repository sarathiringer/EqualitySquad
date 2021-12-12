import React, { Component } from 'react';
import pic from './pic_frontpage.jpg'

export class About extends Component {
  static displayName = About.name;

  constructor(props) {
    super(props);
    this.state = { forecasts: [], loading: true };
  }

    render() {
        return (
            <div>
                <img src={pic} alt='picture' />
            </div>
        );
  }
}
