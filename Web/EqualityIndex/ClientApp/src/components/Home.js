import React, { Component } from 'react';
import picIndex from './pic_index.jpg'

export class Home extends Component {
  static displayName = Home.name;

  render () {
    return (
        <div>
            <h3>Gender equality index for the whole Swedish tech industry</h3>
            <iframe src="https://dashboardequalityindex.azurewebsites.net/" width="1200" height="1500"/>
      </div>
    );
  }
}
