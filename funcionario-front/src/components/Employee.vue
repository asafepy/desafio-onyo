<template>
  <div>
    <v-toolbar flat color="white">
      <v-toolbar-title>CRUD Funcionários</v-toolbar-title>
      <v-divider
        class="mx-2"
        inset
        vertical
      ></v-divider>
      <v-spacer></v-spacer>
      <v-dialog v-model="dialog" max-width="500px">
        <v-btn slot="activator" color="primary" dark class="mb-2">+</v-btn>
        <v-card>
          <v-card-title>
            <span class="headline">{{ formTitle }}</span>
          </v-card-title>

          <v-card-text>
            <v-container grid-list-md>
              <v-layout wrap>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.name" label="Nome"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.surname" label="Sobrenome"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.role" label="Cargo"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.cep" label="CEP"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.bairro" label="Bairro"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.localidade" label="Localidade"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.uf" label="UF"></v-text-field>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" flat @click="close">Cancel</v-btn>
            <v-btn color="blue darken-1" flat @click="save">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-toolbar>
    <v-data-table
      :headers="headers"
      :items="desserts"
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td class="text-xs-right">{{ props.item.name }}</td>
        <td class="text-xs-right">{{ props.item.surname }}</td>
        <td class="text-xs-right">{{ props.item.role }}</td>
        <td class="text-xs-right">{{ props.item.cep }}</td>
        <td class="text-xs-right">{{ props.item.bairro }}</td>
        <td class="text-xs-right">{{ props.item.localidade }}</td>
        <td class="text-xs-right">{{ props.item.uf }}</td>
        <td class="justify-center layout px-0">
          <v-icon
            small
            class="mr-2"
            @click="editItem(props.item)"
          >
            editar
          </v-icon>
          <v-icon
            small
            @click="deleteItem(props.item)"
          >
            deletar
          </v-icon>
        </td>
      </template>
      <template slot="no-data">
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
  </div>
</template>


<script>
  export default {
    data: () => ({
      dialog: false,
      headers: [
        { text: 'Nome', value: 'calories' },
        { text: 'Sobrenome', value: 'surname' },
        { text: 'Cargo', value: 'role' },
        { text: 'CEP', value: 'cep' },
        { text: 'Bairro', value: 'bairro'},
        { text: 'Localidade', value: 'localidade'},
        { text: 'UF', value: 'uf'}
      ],
      Employee: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        surname: '',
        role: '',
        cep: '',
        bairro: '',
        localidade: '',
        uf: '',

      },
      defaultItem: {
        name: '',
        surname: '',
        role: '',
        cep: '',
        bairro: '',
        localidade: '',
        uf: '',
      }
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Novo Funcionário' : 'Editar Funcionário'
      }
    },

    watch: {
      dialog (val) {
        val || this.close()
      }
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        this.axios.get('/funcionario/')
          .then(response => {
            this.Employee = response.data['results']
          })
          .catch(error => {
            console.log(error)
          })
      },

      editItem (item) {
        this.editedIndex = this.desserts.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.desserts.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.desserts.splice(index, 1)
      },

      close () {
        this.dialog = false
        setTimeout(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        }, 300)
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.desserts[this.editedIndex], this.editedItem)
        } else {
          this.desserts.push(this.editedItem)
        }
        this.close()
      }
    }
  }
</script>