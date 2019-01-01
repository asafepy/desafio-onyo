

<template>
  <v-app>
    <v-navigation-drawer
      persistent
      :mini-variant="miniVariant"
      :clipped="clipped"
      v-model="drawer"
      enable-resize-watcher
      fixed
      app
    >
      <v-list>
        <v-list-tile
          value="true"
          v-for="(item, i) in items"
          :key="i"
          :to=item.to
        >
          <v-list-tile-action>
            <v-icon v-html="item.icon"></v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title v-text="item.title"></v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar
      app
      :clipped-left="clipped"
    >
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>

      <v-spacer></v-spacer>
      <v-toolbar-title v-text="title"></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu bottom left>
        <v-btn slot="activator" dark icon  >
          <v-avatar size="32px" tile>
            <img src="https://image.flaticon.com/icons/png/512/17/17004.png" alt="Vuetify">
          </v-avatar>
        </v-btn>
        <v-list>
          <v-list-tile v-for="(item, i) in headerMenu" :key="i" @click="logout(item.title)">
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>


    </v-toolbar>
    <v-content>
      <router-view/>
    </v-content>
    <v-footer :fixed="fixed" app>
      <span>&copy; 2017</span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        clipped: true,
        drawer: true,
        fixed: false,
        items: [
          {
            icon: 'home',
            title: 'Dashboard',
            to: '/'
          },
          {
            icon: 'move_to_inbox',
            title: 'Employee',
            to: 'funcionario-list'
          }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Fundo Estadual de Recursos Hídricos',
        headerMenu: [{title: 'Sair'}]
      }
    },
    name: 'App',
  }
</script>