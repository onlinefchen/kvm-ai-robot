# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 15:35:28

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 155
- **总 Thread 数**: 29
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 24 threads (128 邮件)
- **RFC**: 1 threads (17 邮件)
- **Bug Report**: 1 threads (2 邮件)
- **Question**: 2 threads (5 邮件)
- **GIT PULL**: 1 threads (3 邮件)

---

## 📌 PATCH

共 24 个 thread

---

### Thread 1: [PATCH v3 00/25] KVM: x86/mmu: TDX post-populate cleanups

**📧 邮件数**: 28 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 16 Oct 2025 17:32:18 -0700

#### 🤖 AI 总结

本 thread 共有 28 封邮件，2 位参与者。

📋 补丁内容：Add the async_ioctl() => unlocked_ioctl() patches, and use the "unlocked"
   variant in the TDX vCPU sub-ioctls so they can take kvm->lock outside of
   vcpu->mutex...

🔑 关键讨论点：
• ne small question:
 : >
 : > What if the memory region passed to KVM_TDX_INIT_MEM_REGION hasn't been pre-
 : > populated?...
• Or we can make KVM_TDX_INIT_MEM_REGION
 : > return error when it finds the region hasn't been pre-populated?...
• u, u64 gpa)
-{
-	struct kvm *kvm = vcpu->kvm;
-	bool is_direct = kvm_is_addr_direct(kvm, gpa);
-	hpa_t root = is_direct ?...

💬 这是一个非常活跃的讨论，有 28 封邮件往来。

#### 📝 邮件列表

1. **[10-16 17:32]** [PATCH v3 00/25] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-16 17:32]** [PATCH v3 01/25] KVM: Make support for kvm_arch_vcpu_async_ioctl() mandatory
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-16 17:32]** [PATCH v3 02/25] KVM: Rename kvm_arch_vcpu_async_ioctl() to kvm_arch_vcpu_unlocked_ioctl()
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-16 17:32]** [PATCH v3 03/25] KVM: TDX: Drop PROVE_MMU=y sanity check on
 to-be-populated mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[10-16 17:32]** [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map guest_memfd
 pfn into TDP MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[10-16 17:32]** [PATCH v3 05/25] Revert "KVM: x86/tdp_mmu: Add a helper function to
 walk down the TDP MMU"
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[10-16 17:32]** [PATCH v3 06/25] KVM: x86/mmu: Rename kvm_tdp_map_page() to kvm_tdp_page_prefault()
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[10-16 17:32]** [PATCH v3 07/25] KVM: TDX: Drop superfluous page pinning in S-EPT management
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[10-16 17:32]** [PATCH v3 08/25] KVM: TDX: Return -EIO, not -EINVAL, on a
 KVM_BUG_ON() condition
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[10-16 17:32]** [PATCH v3 09/25] KVM: TDX: Fold tdx_sept_drop_private_spte() into tdx_sept_remove_private_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[10-16 17:32]** [PATCH v3 10/25] KVM: x86/mmu: Drop the return code from kvm_x86_ops.remove_external_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[10-16 17:32]** [PATCH v3 11/25] KVM: TDX: Avoid a double-KVM_BUG_ON() in tdx_sept_zap_private_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[10-16 17:32]** [PATCH v3 12/25] KVM: TDX: Use atomic64_dec_return() instead of a
 poor equivalent
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[10-16 17:32]** [PATCH v3 13/25] KVM: TDX: Fold tdx_mem_page_record_premap_cnt() into
 its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[10-16 17:32]** [PATCH v3 14/25] KVM: TDX: Bug the VM if extended the initial
 measurement fails
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[10-16 17:32]** [PATCH v3 15/25] KVM: TDX: ADD pages to the TD image while populating
 mirror EPT entries
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[10-16 17:32]** [PATCH v3 16/25] KVM: TDX: Fold tdx_sept_zap_private_spte() into tdx_sept_remove_private_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[10-16 17:32]** [PATCH v3 17/25] KVM: TDX: Combine KVM_BUG_ON + pr_tdx_error() into TDX_BUG_ON()
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[10-16 17:32]** [PATCH v3 18/25] KVM: TDX: Derive error argument names from the local
 variable names
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[10-16 17:32]** [PATCH v3 19/25] KVM: TDX: Assert that mmu_lock is held for write
 when removing S-EPT entries
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[10-16 17:32]** [PATCH v3 20/25] KVM: TDX: Add macro to retry SEAMCALLs when forcing
 vCPUs out of guest
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[10-16 17:32]** [PATCH v3 21/25] KVM: TDX: Add tdx_get_cmd() helper to get and
 validate sub-ioctl command
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[10-16 17:32]** [PATCH v3 22/25] KVM: TDX: Convert INIT_MEM_REGION and INIT_VCPU to
 "unlocked" vCPU ioctl
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[10-16 17:32]** [PATCH v3 23/25] KVM: TDX: Use guard() to acquire kvm->lock in tdx_vm_ioctl()
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[10-16 17:32]** [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all" the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[10-16 17:32]** [PATCH v3 25/25] KVM: TDX: Fix list_add corruption during vcpu_load()
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[10-17 11:12]** Re: [PATCH v3 01/25] KVM: Make support for
 kvm_arch_vcpu_async_ioctl() mandatory
   - 发件人: Claudio Imbrenda <imbrenda@linux.ibm.com>
28. **[10-17 11:13]** Re: [PATCH v3 02/25] KVM: Rename kvm_arch_vcpu_async_ioctl() to
 kvm_arch_vcpu_unlocked_ioctl()
   - 发件人: Claudio Imbrenda <imbrenda@linux.ibm.com>

---

### Thread 2: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support

**📧 邮件数**: 27 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 16 Oct 2025 10:28:41 -0700

#### 🤖 AI 总结

本 thread 共有 27 封邮件，4 位参与者。

📋 补丁内容：add a new iterator
macros in ...

💬 这是一个非常活跃的讨论，有 27 封邮件往来。

#### 📝 邮件列表

1. **[10-16 10:28]** [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-16 10:28]** [PATCH v13 01/12] KVM: guest_memfd: Rename "struct kvm_gmem" to
 "struct gmem_file"
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-16 10:28]** [PATCH v13 02/12] KVM: guest_memfd: Add macro to iterate over
 gmem_files for a mapping/inode
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-16 10:28]** [PATCH v13 03/12] KVM: guest_memfd: Use guest mem inodes instead of
 anonymous inodes
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[10-16 10:28]** [PATCH v13 04/12] KVM: guest_memfd: Add slab-allocated inode cache
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[10-16 10:28]** [PATCH v13 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[10-16 10:28]** [PATCH v13 06/12] KVM: selftests: Define wrappers for common syscalls
 to assert success
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[10-16 10:28]** [PATCH v13 07/12] KVM: selftests: Report stacktraces SIGBUS, SIGSEGV,
 SIGILL, and SIGFPE by default
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[10-16 10:28]** [PATCH v13 08/12] KVM: selftests: Add additional equivalents to
 libnuma APIs in KVM's numaif.h
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[10-16 10:28]** [PATCH v13 09/12] KVM: selftests: Use proper uAPI headers to pick up
 mempolicy.h definitions
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[10-16 10:28]** [PATCH v13 10/12] KVM: selftests: Add helpers to probe for NUMA
 support, and multi-node systems
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[10-16 10:28]** [PATCH v13 11/12] KVM: selftests: Add guest_memfd tests for mmap and
 NUMA policy support
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[10-16 10:28]** [PATCH v13 12/12] KVM: guest_memfd: Add gmem_inode.flags field
 instead of using i_private
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[10-16 20:08]** Re: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Miguel Ojeda <miguel.ojeda.sandonis@gmail.com>
15. **[10-16 13:28]** Re: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[10-16 23:07]** Re: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Miguel Ojeda <miguel.ojeda.sandonis@gmail.com>
17. **[10-16 16:57]** Re: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Ackerley Tng <ackerleytng@google.com>
18. **[10-17 02:09]** Re: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Miguel Ojeda <miguel.ojeda.sandonis@gmail.com>
19. **[10-17 15:01]** Re: [PATCH v13 01/12] KVM: guest_memfd: Rename "struct kvm_gmem" to
 "struct gmem_file"
   - 发件人: Garg, Shivank <shivankg@amd.com>
20. **[10-17 15:04]** Re: [PATCH v13 02/12] KVM: guest_memfd: Add macro to iterate over
 gmem_files for a mapping/inode
   - 发件人: Garg, Shivank <shivankg@amd.com>
21. **[10-17 15:21]** Re: [PATCH v13 06/12] KVM: selftests: Define wrappers for common
 syscalls to assert success
   - 发件人: Garg, Shivank <shivankg@amd.com>
22. **[10-17 15:23]** Re: [PATCH v13 07/12] KVM: selftests: Report stacktraces SIGBUS,
 SIGSEGV, SIGILL, and SIGFPE by default
   - 发件人: Garg, Shivank <shivankg@amd.com>
23. **[10-17 15:42]** Re: [PATCH v13 08/12] KVM: selftests: Add additional equivalents to
 libnuma APIs in KVM's numaif.h
   - 发件人: Garg, Shivank <shivankg@amd.com>
24. **[10-17 16:05]** Re: [PATCH v13 09/12] KVM: selftests: Use proper uAPI headers to pick
 up mempolicy.h definitions
   - 发件人: Garg, Shivank <shivankg@amd.com>
25. **[10-17 16:31]** Re: [PATCH v13 12/12] KVM: guest_memfd: Add gmem_inode.flags field
 instead of using i_private
   - 发件人: Garg, Shivank <shivankg@amd.com>
26. **[10-17 09:18]** Re: [PATCH v13 09/12] KVM: selftests: Use proper uAPI headers to pick
 up mempolicy.h definitions
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[10-17 09:49]** Re: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 3: [PATCH v12 00/12] KVM: guest_memfd: Add NUMA mempolicy support

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Tue,  7 Oct 2025 15:14:08 -0700

#### 🤖 AI 总结

本 thread 共有 8 封邮件，3 位参与者。

📋 补丁内容：this series (I want to keep this
version KVM focused, and AFAICT there is nothing left to discuss in the prep
paches)...

🔑 关键讨论点：
• {
+#ifdef CONFIG_NUMA
+	struct mempolicy *mpol;
+
+	mpol = mpol_shared_policy_lookup(&gi->policy, index);
+	return mpol ?...
• com> writes:


How about kvm_gmem_get_index_policy() instead, since the policy is keyed
by index?...
• Should we be returning NULL if no shared policy was defined?...

💬 讨论有 8 轮回复。

#### 📝 邮件列表

1. **[10-07 15:14]** [PATCH v12 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-07 15:14]** [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-09 15:15]** Re: [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Ackerley Tng <ackerleytng@google.com>
4. **[10-10 13:27]** Re: [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Garg, Shivank <shivankg@amd.com>
5. **[10-10 13:33]** Re: [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[10-10 14:57]** Re: [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Ackerley Tng <ackerleytng@google.com>
7. **[10-13 01:30]** Re: [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Garg, Shivank <shivankg@amd.com>
8. **[10-15 09:56]** Re: [PATCH v12 05/12] KVM: guest_memfd: Enforce NUMA mempolicy using
 shared policy
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 4: [PATCH 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 13 Oct 2025 09:32:04 +0100

#### 🤖 AI 总结

本 thread 共有 8 封邮件，2 位参与者。

📋 补丁内容：Peter reported[1] that restoring a GICv2 VM fails badly, and correctly
points out that ID_PFR1_EL1.GIC isn't writable, while its 64bit
equivalent is. I broke that in 6.12....

💬 讨论有 8 轮回复。

#### 📝 邮件列表

1. **[10-13 09:32]** [PATCH 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-13 09:32]** [PATCH 1/3] KVM: arm64: Make ID_PFR1_EL1.GIC writable
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[10-13 09:32]** [PATCH 2/3] KVM: arm64: Set ID_{AA64PFR0,PFR1}_EL1.GIC when GICv3 is configured
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[10-13 09:32]** [PATCH 3/3] KVM: arm64: Limit clearing of ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[10-14 11:21]** [PATCH 0/3] set_id_regs cleanup
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[10-14 11:21]** [PATCH 1/3] KVM: arm64: selftests: Count test_guest_reg_read() as a test
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[10-14 11:21]** [PATCH 2/3] KVM: arm64: selftests: Remove ARM64_FEATURE_FIELD_BITS and its last user
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[10-14 11:21]** [PATCH 3/3] KVM: arm64: selftests: Consider all 7 possible levels of cache
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

### Thread 5: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Thu,  9 Oct 2025 13:12:39 +0100

#### 🤖 AI 总结

本 thread 共有 7 封邮件，4 位参与者。

📋 补丁内容：implement FEAT_VHE
and not FEAT_E2H0:

- either they advertise it via ID_AA64MMFR4_EL1...

💬 讨论有 7 轮回复。

#### 📝 邮件列表

1. **[10-09 13:12]** [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-09 14:30]** Re: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[10-10 10:22]** Re: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[10-10 10:36]** Re: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[10-13 12:17]** Re: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[10-14 09:49]** Re: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[10-14 09:53]** Re: [PATCH] arm64: Revamp HCR_EL2.E2H RES1 detection
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v7 00/28] Tracefs support for pKVM

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  3 Oct 2025 14:37:57 +0100

#### 🤖 AI 总结

本 thread 共有 6 封邮件，2 位参与者。

📋 补丁内容：This series first introduces a new generic way of creating remote events and
remote buffers...

🔑 关键讨论点：
• racefs(struct dentry *d, void *unused)
+{
+	return tracefs_create_file("write_event", 0200, d, NULL, &write_event_fops) ?...
• Do you want a v8 now (and with your previous comment) or shall I wait a bit more?...

💬 讨论有 6 轮回复。

#### 📝 邮件列表

1. **[10-03 14:37]** [PATCH v7 00/28] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[10-03 14:38]** [PATCH v7 14/28] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[10-16 17:06]** Re: [PATCH v7 14/28] tracing: Add a trace remote module for testing
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
4. **[10-16 17:11]** Re: [PATCH v7 14/28] tracing: Add a trace remote module for testing
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
5. **[10-17 09:36]** Re: [PATCH v7 14/28] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[10-17 05:14]** Re: [PATCH v7 14/28] tracing: Add a trace remote module for testing
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 7: [PATCH v2 0/4] KVM ARM64 pre_fault_memory

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 13 Oct 2025 16:14:57 +0100

#### 🤖 AI 总结

本 thread 共有 6 封邮件，2 位参与者。

📋 补丁内容：This patch series adds ARM64 support for the KVM_PRE_FAULT_MEMORY
feature, which was previously only available on x86 [1]...

🔑 关键讨论点：
• erspace_mem_region_add(vm, VM_MEM_SRC_ANONYMOUS,
-				    guest_test_phys_mem, TEST_SLOT, TEST_NPAGES,
-				    private ?...
• test_num_pages,
+				    p->private ?...
• test_num_pages,
 				    p->private ?...

💬 讨论有 6 轮回复。

#### 📝 邮件列表

1. **[10-13 16:14]** [PATCH v2 0/4] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[10-13 16:14]** [PATCH v2 1/4] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[10-13 16:14]** [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
4. **[10-13 16:15]** [PATCH v2 3/4] KVM: selftests: Enable pre_fault_memory_test for arm64
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
5. **[10-13 16:15]** [PATCH v2 4/4] KVM: selftests: Add option for different backing in pre-fault tests
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
6. **[10-16 15:01]** Re: [PATCH v2 1/4] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 8: [PATCH] KVM: arm64: selftests: Sync ID_AA64PFR1, MPIDR, CLIDR in guest

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Sun, 12 Oct 2025 23:43:52 +0800

#### 🤖 AI 总结

本 thread 共有 5 封邮件，3 位参与者。

📋 补丁内容：We forgot to sync several registers (ID_AA64PFR1, MPIDR, CLIDR) in guest to
make sure that the guest had seen the written value....

🔑 关键讨论点：
• Hi Zenghui,

On 10/12/25 16:43, Zenghui Yu wrote:

Why did you choose this position in the list for these 2?...
• How about adding a ksft_test_result_pass("%s\n", __func__) and
bumping the number of tests?...

#### 📝 邮件列表

1. **[10-12 23:43]** [PATCH] KVM: arm64: selftests: Sync ID_AA64PFR1, MPIDR, CLIDR in guest
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[10-13 13:20]** Re: [PATCH] KVM: arm64: selftests: Sync ID_AA64PFR1, MPIDR, CLIDR in
 guest
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[10-13 17:14]** Re: [PATCH] KVM: arm64: selftests: Sync ID_AA64PFR1, MPIDR, CLIDR in
 guest
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[10-13 17:56]** Re: [PATCH] KVM: arm64: selftests: Sync ID_AA64PFR1, MPIDR, CLIDR in guest
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[10-14 14:59]** Re: [PATCH] KVM: arm64: selftests: Sync ID_AA64PFR1, MPIDR, CLIDR in
 guest
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 9: [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 13 Oct 2025 18:59:00 +0000

#### 🤖 AI 总结

本 thread 共有 5 封邮件，2 位参与者。

📋 补丁内容：implement SIGBUS on arm64 as well, but
  Marc preferred KVM exit over signal [3]...

🔑 关键讨论点：
• in firmware");
+
+	if (access(EINJ_ETYPE, R_OK | W_OK) == -1)
+		ksft_test_result_skip("EINJ module probably not loaded?...
• Above needs an ending like '.' or ':'....

#### 📝 邮件列表

1. **[10-13 18:59]** [PATCH v4 0/3] VMM can handle guest SEA via KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
2. **[10-13 18:59]** [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[10-13 18:59]** [PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[10-13 18:59]** [PATCH v4 3/3] Documentation: kvm: new UAPI for handling SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
5. **[10-13 18:51]** Re: [PATCH v4 3/3] Documentation: kvm: new UAPI for handling SEA
   - 发件人: Randy Dunlap <rdunlap@infradead.org>

---

### Thread 10: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 1 Oct 2025 11:14:23 -0700

#### 🤖 AI 总结

本 thread 共有 4 封邮件，2 位参与者。

📋 补丁内容：On Fri, Sep 26, 2025, Sandipan Das wrote:...

🔑 关键讨论点：
• The function name kvm_need_pmc_intercept() seems a little bit misleading...
• Maybe something like kvm_need_any_pmc_intercept()?...
• Yeah, I don't love kvm_need_pmc_intercept() either.  But kvm_need_global_intercept()...

#### 📝 邮件列表

1. **[10-01 11:14]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-09 10:19]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
3. **[10-15 11:48]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-16 08:04]** Re: [PATCH v5 32/44] KVM: x86/pmu: Disable interception of select PMU
 MSRs for mediated vPMUs
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>

---

### Thread 11: [PATCH V6 0/3] arm64/sysreg: Clean up TCR_EL1 field macros

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 13 Oct 2025 10:59:42 +0530

#### 🤖 AI 总结

本 thread 共有 4 封邮件，1 位参与者。

🔑 关键讨论点：
• d)
 {
-	return read_tcr() & TCR_DS;
+	return read_tcr() & TCR_EL1_DS;
 }
 
 #define PTE_MAYBE_SHARED	(lpa2_is_enabled() ?...

#### 📝 邮件列表

1. **[10-13 10:59]** [PATCH V6 0/3] arm64/sysreg: Clean up TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[10-13 10:59]** [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with TCR_EL1_NFD[0|1]
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[10-13 10:59]** [PATCH V6 2/3] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[10-13 10:59]** [PATCH V6 3/3] KVM: arm64: Move inside all required TCR_XXX macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 12: [PATCH] KVM: selftests: fix ITS collection target addresses in vgic_lpi_stress

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 17 Oct 2025 18:19:18 +0200

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

📋 补丁内容：Fix by left-shifting the vCPU parameter received by its_send_mapc_cmd
16 bits before passing it into its_encode_target for encoding...

#### 📝 邮件列表

1. **[10-17 18:19]** [PATCH] KVM: selftests: fix ITS collection target addresses in vgic_lpi_stress
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
2. **[10-17 18:06]** Re: [PATCH] KVM: selftests: fix ITS collection target addresses in vgic_lpi_stress
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH] KVM: arm64: selftests: Allocate vcpus with correct size

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  8 Oct 2025 23:45:20 +0800

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

📋 补丁内容：Fix the
allocation by using the correct size...

#### 📝 邮件列表

1. **[10-08 23:45]** [PATCH] KVM: arm64: selftests: Allocate vcpus with correct size
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[10-13 17:56]** Re: [PATCH] KVM: arm64: selftests: Allocate vcpus with correct size
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] KVM: arm64: gic-v3: Only set ICH_HCR traps for v2-on-v3 or v3
 guests

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 7 Oct 2025 16:07:13 +0000

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

#### 📝 邮件列表

1. **[10-07 16:07]** [PATCH] KVM: arm64: gic-v3: Only set ICH_HCR traps for v2-on-v3 or v3
 guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[10-13 17:56]** Re: [PATCH] KVM: arm64: gic-v3: Only set ICH_HCR traps for v2-on-v3 or v3 guests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH] Documentation: KVM: Update GICv3 docs for GICv5 hosts

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 7 Oct 2025 15:48:54 +0000

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

📋 补丁内容：Update the GICv3
documentation to reflect this now that GICv3 guests are supports on
compatible GICv5 hosts...

#### 📝 邮件列表

1. **[10-07 15:48]** [PATCH] Documentation: KVM: Update GICv3 docs for GICv5 hosts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[10-13 17:56]** Re: [PATCH] Documentation: KVM: Update GICv3 docs for GICv5 hosts
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH] KVM: arm64: selftests: Actually enable IRQs in vgic_lpi_stress

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  7 Oct 2025 12:52:55 -0700

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

📋 补丁内容：vgic_lpi_stress rather hilariously leaves IRQs disabled for the duration
of the test. While the ITS translation of MSIs happens regardless of
this, for completeness the guest should actually handle th...

#### 📝 邮件列表

1. **[10-07 12:52]** [PATCH] KVM: arm64: selftests: Actually enable IRQs in vgic_lpi_stress
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[10-13 17:56]** Re: [PATCH] KVM: arm64: selftests: Actually enable IRQs in vgic_lpi_stress
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH 00/13] KVM: arm64: De-specialise the timer UAPI

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 29 Sep 2025 17:04:44 +0100

#### 🤖 AI 总结

本 thread 共有 2 封邮件，1 位参与者。

📋 补丁内容：This series aims at fixing all of the above, moving the handling of
the timer sysregs to sys_regs...

#### 📝 邮件列表

1. **[09-29 17:04]** [PATCH 00/13] KVM: arm64: De-specialise the timer UAPI
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-13 17:55]** Re: [PATCH 00/13] KVM: arm64: De-specialise the timer UAPI
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH v2] KVM: arm64: Guard PMSCR_EL1 initialization with SPE presence check

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 10 Oct 2025 23:17:07 +0530

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

#### 📝 邮件列表

1. **[10-10 23:17]** [PATCH v2] KVM: arm64: Guard PMSCR_EL1 initialization with SPE presence check
   - 发件人: Mukesh Ojha <mukesh.ojha@oss.qualcomm.com>
2. **[10-13 17:56]** Re: [PATCH v2] KVM: arm64: Guard PMSCR_EL1 initialization with SPE presence check
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH 00/10] KVM: selftests: Convert to kernel-style types

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 17 Oct 2025 15:38:45 -0700

#### 🤖 AI 总结

本 thread 共有 1 封邮件，1 位参与者。

📋 补丁内容：On Thu, May 1, 2025 at 2:03 PM Sean Christopherson <seanjc@google.com> wrote:...

#### 📝 邮件列表

1. **[10-17 15:38]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: David Matlack <dmatlack@google.com>

---

### Thread 20: [PATCH v11 00/42] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 17 Oct 2025 15:55:01 +0100

#### 🤖 AI 总结

本 thread 共有 1 封邮件，1 位参与者。

📋 补丁内容：update to fix as the RMM will need to in some cases
   emulate the PMU registers...

#### 📝 邮件列表

1. **[10-17 15:55]** [PATCH v11 00/42] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 21: [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory share

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 17 Oct 2025 07:57:10 +0000

#### 🤖 AI 总结

本 thread 共有 1 封邮件，1 位参与者。

📋 补丁内容：Verify the offset to prevent OOB access in the hypervisor
FF-A buffer in case an untrusted large enough value
[U32_MAX - sizeof(struct ffa_composite_mem_region) + 1, U32_MAX]
is set from the host kern...

#### 📝 邮件列表

1. **[10-17 07:57]** [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory share
   - 发件人: Sebastian Ene <sebastianene@google.com>

---

### Thread 22: [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 16 Oct 2025 17:45:41 +0100

#### 🤖 AI 总结

本 thread 共有 1 封邮件，1 位参与者。

📋 补丁内容：There's currently no verification for host issued ranges in most of the
pKVM memory transitions. The end boundary might therefore be subject to
overflow and later checks could be evaded....

#### 📝 邮件列表

1. **[10-16 17:45]** [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 23: [PATCH 0/2] KVM: arm64: nv: FGT traps of MDSCR_EL1

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 13 Oct 2025 17:56:06 +0100

#### 🤖 AI 总结

本 thread 共有 1 封邮件，1 位参与者。

📋 补丁内容：On Wed, 24 Sep 2025 16:51:48 -0700, Oliver Upton wrote:...

#### 📝 邮件列表

1. **[10-13 17:56]** Re: [PATCH 0/2] KVM: arm64: nv: FGT traps of MDSCR_EL1
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU tables

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 12 Oct 2025 23:51:25 -0700

#### 🤖 AI 总结

本 thread 共有 1 封邮件，1 位参与者。

📋 补丁内容：This patch adds a maple-tree-based lookup that records canonical-IPA to
shadow-IPA mappings whenever a page is mapped into any shadow (L2)
table...

#### 📝 邮件列表

1. **[10-12 23:51]** [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU tables
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device

**📧 邮件数**: 17 | **👥 参与者**: 6 | **📅 开始时间**: Fri, 10 Oct 2025 07:10:58 -0500

#### 🤖 AI 总结

本 thread 共有 17 封邮件，6 位参与者。

💭 这是一个征求意见（RFC）的讨论。

💬 这是一个非常活跃的讨论，有 17 封邮件往来。

#### 📝 邮件列表

1. **[10-10 07:10]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jeremy Linton <jeremy.linton@arm.com>
2. **[10-10 10:59]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
3. **[10-10 10:28]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jeremy Linton <jeremy.linton@arm.com>
4. **[10-10 12:30]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
5. **[10-10 10:50]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jeremy Linton <jeremy.linton@arm.com>
6. **[10-10 11:44]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: dan.j.williams <dan.j.williams@intel.com>
7. **[10-10 19:34]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
8. **[10-13 15:42]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jeremy Linton <jeremy.linton@arm.com>
9. **[10-15 15:22]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
10. **[10-15 11:58]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
11. **[10-15 08:50]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
12. **[10-15 13:57]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
13. **[10-15 09:15]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
14. **[10-15 14:37]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
15. **[10-15 11:19]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm
 platform device
   - 发件人: James Bottomley <James.Bottomley@HansenPartnership.com>
16. **[10-15 18:03]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Greg KH <gregkh@linuxfoundation.org>
17. **[10-15 13:34]** Re: [RFC PATCH v1 11/38] KVM: arm64: CCA: register host tsm platform
 device
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: Saving and restoring state of a KVM VM using GICv2 fails

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 10 Oct 2025 16:33:45 +0100

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

#### 📝 邮件列表

1. **[10-10 16:33]** Saving and restoring state of a KVM VM using GICv2 fails
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
2. **[10-12 18:14]** Re: Saving and restoring state of a KVM VM using GICv2 fails
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Question

共 2 个 thread

---

### Thread 1: Question about heterogeneous VM live migration

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 16 Oct 2025 10:00:07 +0800

#### 🤖 AI 总结

本 thread 共有 3 封邮件，2 位参与者。

❓ 这是一个技术问题讨论。

#### 📝 邮件列表

1. **[10-16 10:00]** Question about heterogeneous VM live migration
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[10-17 14:12]** Re: Question about heterogeneous VM live migration
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[10-18 11:17]** Re: Question about heterogeneous VM live migration
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 2: [Question] Received vtimer interrupt but ISTATUS is 0

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 14 Oct 2025 22:45:37 +0800

#### 🤖 AI 总结

本 thread 共有 2 封邮件，2 位参与者。

❓ 这是一个技术问题讨论。

🔑 关键讨论点：
• errupt that we cannot trust having taken an
interrupt, how long until we can trust that what we have is actually
correct?...
• How does it work when context-switching from a vcpu that has a pending
timer interrupt to one that doesn't?...

#### 📝 邮件列表

1. **[10-14 22:45]** [Question] Received vtimer interrupt but ISTATUS is 0
   - 发件人: Kunkun Jiang <jiangkunkun@huawei.com>
2. **[10-14 17:32]** Re: [Question] Received vtimer interrupt but ISTATUS is 0
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.18, take #1

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 14 Oct 2025 13:28:57 +0100

#### 🤖 AI 总结

本 thread 共有 3 封邮件，3 位参与者。

#### 📝 邮件列表

1. **[10-14 13:28]** [GIT PULL] KVM/arm64 fixes for 6.18, take #1
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-15 15:31]** Re: [GIT PULL] KVM/arm64 fixes for 6.18, take #1
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
3. **[10-15 07:04]** Re: [GIT PULL] KVM/arm64 fixes for 6.18, take #1
   - 发件人: Sean Christopherson <seanjc@google.com>

---

