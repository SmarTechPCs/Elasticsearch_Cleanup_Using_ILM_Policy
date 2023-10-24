# Error codes
ERROR_DELETE_POLICY = 10
ERROR_CREATE_POLICY = 20
ERROR_ATTACH_POLICY = 30


class DeletePolicyException(Exception):
    def __init__(self, error, message="Failed to deleted policy"):
        self.error_message = f"{message}: {error}"
        self.error_code = ERROR_DELETE_POLICY
        super().__init__(self.error_message)


class CreatePolicyException(Exception):
    def __init__(self, error, message="Failed to create policy"):
        self.error_message = f"{message}: {error}"
        self.error_code = ERROR_CREATE_POLICY
        super().__init__(self.error_message)


class AttachPolicyException(Exception):
    def __init__(self, error, message="Failed to attach policy"):
        self.error_message = f"{message}: {error}"
        self.error_code = ERROR_ATTACH_POLICY
        super().__init__(self.error_message)
