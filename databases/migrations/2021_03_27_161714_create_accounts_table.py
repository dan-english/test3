from masoniteorm.migrations import Migration

class CreateAccountsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('accounts') as table:
            table.increments('id')
            table.string('email')
            table.string('access_token')
            table.string('scopes')
            table.string('type')
            table.string('provider')
            table.string('nylas_account_id')
            table.boolean('valid').default(False)
            table.integer('user_id').unsigned()

            table.foreign('user_id').references('id').on('users')

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('accounts')

