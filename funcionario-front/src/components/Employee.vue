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
                  <v-text-field v-model="editedItem.address.cep" @blur="get_cep(editedItem.address.cep)" label="CEP"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.address.bairro" label="Bairro"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.address.localidade" label="Localidade"></v-text-field>
                </v-flex>
                <v-flex xs12 sm6 md4>
                  <v-text-field v-model="editedItem.address.uf" label="UF"></v-text-field>
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
      :items="employeeItems"
      class="elevation-1"
    >
      <template slot="items" slot-scope="props">
        <td class="text-xs-left">{{ props.item.name }}</td>
        <td class="text-xs-left">{{ props.item.surname }}</td>
        <td class="text-xs-left">{{ props.item.role }}</td>
        <td class="text-xs-left">{{ props.item.address.cep }}</td>
        <td class="text-xs-left">{{ props.item.address.bairro }}</td>
        <td class="text-xs-left">{{ props.item.address.localidade }}</td>
        <td class="text-xs-left">{{ props.item.address.uf }}</td>
        <td class="justify-center layout px-0">
          <v-icon
            small
            class="mr-2"
            @click="editItem(props.item)"
          >
            edit
          </v-icon>
          <v-icon
            small
            @click="deleteItem(props.item)"
          >
            delete
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
        { text: 'UF', value: 'uf'},
        { text: 'Ações', value: 'name', sortable: false }

      ],
      employeeItems: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        surname: '',
        role: '',
        address:{
          cep: '',
          bairro: '',
          localidade: '',
          uf: '',
        }

      },
      defaultItem: {
        name: '',
        surname: '',
        role: '',
        address:{
          cep: '',
          bairro: '',
          localidade: '',
          uf: '',
        }
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
            this.employeeItems = response.data
          })
          .catch(error => {
            console.log(error)
          })
      },

      get_cep() {
        
        this.axios.get(`/cep/${this.editedItem.address.cep}/`)
        .then(response => { 
          this.editedItem.address.bairro = response.data.bairro
          this.editedItem.address.localidade = response.data.localidade
          this.editedItem.address.uf = response.data.uf
        })
        .catch(error => {
          console.log(error)
        })
      },

      editItem (item) {
        this.editedIndex = this.employeeItems.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.employeeItems.indexOf(item)
        confirm('Are you sure you want to delete this item?') && this.employeeItems.splice(index, 1)
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
  
          this.axios.put('/funcionario/', {
            name: this.editedItem.name,
            surname: this.editedItem.surname,
            role: this.editedItem.role,
            address:{
              cep: this.editedItem.address.cep,
              bairro: this.editedItem.address.bairro,
              localidade: this.editedItem.address.localidade,
              uf: this.editedItem.address.uf
            }
          })
          .then(response => { 
            Object.assign(this.employeeItems[this.editedIndex], this.editedItem)
          })
          .catch(error => {
            console.log(error)
          })

        } else {

        this.axios.post('/funcionario/', {
          name: this.editedItem.name,
          surname: this.editedItem.surname,
          role: this.editedItem.role,
          address:{
            cep: this.editedItem.address.cep,
            bairro: this.editedItem.address.bairro,
            localidade: this.editedItem.address.localidade,
            uf: this.editedItem.address.uf
          }
        })
        .then(response => { 
          this.employeeItems.push(response.data)
        })
        .catch(error => {
          console.log(error)
        })
          
        }
        this.close()
      }
    }
  }
</script>