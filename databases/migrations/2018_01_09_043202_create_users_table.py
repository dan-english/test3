from masoniteorm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """Run the migrations."""
        with self.schema.create("users") as table:
            table.increments('id')
            table.string('name')
            table.string('email').unique()
            table.string('password')
            table.string('remember_token').nullable()
            table.boolean('enabled').default(False)
            table.string('avatar').default(' ')
            table.string('mobile_number').default(' ')
            table.string('time_zone').default(' ')
            table.string('access_token').default(' ')
            table.string('nylas_account_id').default(' ')
            table.text('open_hours').nullable()
            table.string('bcc_addresses').default(' ')
            table.string('language').default(' ')
            table.string('currency').default('usd')


            table.timestamp('verified_at').nullable()
            table.timestamps()

    def down(self):
        """Revert the migrations."""
        self.schema.drop("users")
