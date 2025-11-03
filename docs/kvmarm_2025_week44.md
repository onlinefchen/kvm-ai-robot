# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-11-03 00:23:44

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 278
- **总 Thread 数**: 27
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 25 threads (273 邮件)
- **Bug Report**: 2 threads (5 邮件)

---

## 📌 PATCH

共 25 个 thread

---

### Thread 1: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups

**📧 邮件数**: 61 | **👥 参与者**: 5 | **📅 开始时间**: Thu, 30 Oct 2025 13:09:23 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）中 TDX（Trusted Domain Extensions）相关的代码清理和改进，主要集中在 TDX 的后填充路径的锁定问题和 API 的改进。

1. **原始 patch/问题的内容**：
   本次讨论的补丁系列（PATCH v4 00/28）主要涉及对 KVM 中 TDX 后填充路径的清理，特别是锁定机制的改进。补丁中提到将 `kvm_arch_vcpu_async_ioctl()` 改为强制性，并重命名为 `kvm_arch_vcpu_unlocked_ioctl()`，以便在 TDX 代码中更好地处理锁定。

2. **之前讨论要点**：
   之前的讨论主要集中在如何确保 KVM 内部的锁定机制能够满足 TDX 模块的要求，特别是在处理多个并发路径时，确保这些路径的互斥性。补丁还涉及到对错误处理的改进，例如在 KVM_BUG_ON() 触发时返回 -EIO 而不是 -EINVAL，以保持 ABI 一致性。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Sean Christopherson 提出了多个补丁，改进了 TDX 的多个方面，包括：
   - 引入新的 API 来映射 guest_memfd pfn 到 TDP MMU。
   - 在处理 S-EPT（Secure EPT）条目时，确保在移除条目时持有写锁。
   - 使用 guard() 宏来简化锁的管理。
   - 处理 TDX 状态转换时，确保所有相关锁被正确持有，以避免竞态条件。
   - 通过合并多个函数来减少冗余代码，提升代码可读性。

整体来看，本周的讨论和补丁提交旨在提高 KVM TDX 的稳定性和性能，同时确保代码的可维护性。

#### 📝 邮件列表

1. **[10-30 13:09]** [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-30 13:09]** [PATCH v4 01/28] KVM: Make support for kvm_arch_vcpu_async_ioctl() mandatory
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-30 13:09]** [PATCH v4 02/28] KVM: Rename kvm_arch_vcpu_async_ioctl() to kvm_arch_vcpu_unlocked_ioctl()
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-30 13:09]** [PATCH v4 03/28] KVM: TDX: Drop PROVE_MMU=y sanity check on
 to-be-populated mappings
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[10-30 13:09]** [PATCH v4 04/28] KVM: x86/mmu: Add dedicated API to map guest_memfd
 pfn into TDP MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[10-30 13:09]** [PATCH v4 05/28] KVM: x86/mmu: WARN if KVM attempts to map into an
 invalid TDP MMU root
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[10-30 13:09]** [PATCH v4 06/28] Revert "KVM: x86/tdp_mmu: Add a helper function to
 walk down the TDP MMU"
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[10-30 13:09]** [PATCH v4 07/28] KVM: x86/mmu: Rename kvm_tdp_map_page() to kvm_tdp_page_prefault()
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[10-30 13:09]** [PATCH v4 08/28] KVM: TDX: Drop superfluous page pinning in S-EPT management
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[10-30 13:09]** [PATCH v4 09/28] KVM: TDX: Return -EIO, not -EINVAL, on a
 KVM_BUG_ON() condition
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[10-30 13:09]** [PATCH v4 10/28] KVM: TDX: Fold tdx_sept_drop_private_spte() into tdx_sept_remove_private_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[10-30 13:09]** [PATCH v4 11/28] KVM: x86/mmu: Drop the return code from kvm_x86_ops.remove_external_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[10-30 13:09]** [PATCH v4 12/28] KVM: TDX: WARN if mirror SPTE doesn't have full RWX
 when creating S-EPT mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[10-30 13:09]** [PATCH v4 13/28] KVM: TDX: Avoid a double-KVM_BUG_ON() in tdx_sept_zap_private_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[10-30 13:09]** [PATCH v4 14/28] KVM: TDX: Use atomic64_dec_return() instead of a
 poor equivalent
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[10-30 13:09]** [PATCH v4 15/28] KVM: TDX: Fold tdx_mem_page_record_premap_cnt() into
 its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[10-30 13:09]** [PATCH v4 16/28] KVM: TDX: ADD pages to the TD image while populating
 mirror EPT entries
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[10-30 13:09]** [PATCH v4 17/28] KVM: TDX: Fold tdx_sept_zap_private_spte() into tdx_sept_remove_private_spte()
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[10-30 13:09]** [PATCH v4 18/28] KVM: TDX: Combine KVM_BUG_ON + pr_tdx_error() into TDX_BUG_ON()
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[10-30 13:09]** [PATCH v4 19/28] KVM: TDX: Derive error argument names from the local
 variable names
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[10-30 13:09]** [PATCH v4 20/28] KVM: TDX: Assert that mmu_lock is held for write
 when removing S-EPT entries
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[10-30 13:09]** [PATCH v4 21/28] KVM: TDX: Add macro to retry SEAMCALLs when forcing
 vCPUs out of guest
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[10-30 13:09]** [PATCH v4 22/28] KVM: TDX: Add tdx_get_cmd() helper to get and
 validate sub-ioctl command
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[10-30 13:09]** [PATCH v4 23/28] KVM: TDX: Convert INIT_MEM_REGION and INIT_VCPU to
 "unlocked" vCPU ioctl
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[10-30 13:09]** [PATCH v4 24/28] KVM: TDX: Use guard() to acquire kvm->lock in tdx_vm_ioctl()
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[10-30 13:09]** [PATCH v4 25/28] KVM: TDX: Don't copy "cmd" back to userspace for KVM_TDX_CAPABILITIES
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[10-30 13:09]** [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all" the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[10-30 13:09]** [PATCH v4 27/28] KVM: TDX: Bug the VM if extending the initial
 measurement fails
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[10-30 13:09]** [PATCH v4 28/28] KVM: TDX: Fix list_add corruption during vcpu_load()
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[10-30 22:17]** Re: [PATCH v4 05/28] KVM: x86/mmu: WARN if KVM attempts to map into
 an invalid TDP MMU root
   - 发件人: Huang, Kai <kai.huang@intel.com>
31. **[10-30 22:20]** Re: [PATCH v4 09/28] KVM: TDX: Return -EIO, not -EINVAL, on a
 KVM_BUG_ON() condition
   - 发件人: Huang, Kai <kai.huang@intel.com>
32. **[10-30 22:26]** Re: [PATCH v4 11/28] KVM: x86/mmu: Drop the return code from
 kvm_x86_ops.remove_external_spte()
   - 发件人: Huang, Kai <kai.huang@intel.com>
33. **[10-30 22:59]** Re: [PATCH v4 12/28] KVM: TDX: WARN if mirror SPTE doesn't have full
 RWX when creating S-EPT mapping
   - 发件人: Huang, Kai <kai.huang@intel.com>
34. **[10-30 23:03]** Re: [PATCH v4 20/28] KVM: TDX: Assert that mmu_lock is held for write
 when removing S-EPT entries
   - 发件人: Huang, Kai <kai.huang@intel.com>
35. **[10-30 23:05]** Re: [PATCH v4 21/28] KVM: TDX: Add macro to retry SEAMCALLs when
 forcing vCPUs out of guest
   - 发件人: Huang, Kai <kai.huang@intel.com>
36. **[10-30 23:06]** Re: [PATCH v4 25/28] KVM: TDX: Don't copy "cmd" back to userspace for
 KVM_TDX_CAPABILITIES
   - 发件人: Huang, Kai <kai.huang@intel.com>
37. **[10-30 23:08]** Re: [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Huang, Kai <kai.huang@intel.com>
38. **[10-30 23:09]** Re: [PATCH v4 27/28] KVM: TDX: Bug the VM if extending the initial
 measurement fails
   - 发件人: Huang, Kai <kai.huang@intel.com>
39. **[10-30 23:12]** Re: [PATCH v4 28/28] KVM: TDX: Fix list_add corruption during
 vcpu_load()
   - 发件人: Huang, Kai <kai.huang@intel.com>
40. **[10-30 23:19]** Re: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Huang, Kai <kai.huang@intel.com>
41. **[10-30 23:20]** Re: [PATCH v4 18/28] KVM: TDX: Combine KVM_BUG_ON + pr_tdx_error()
 into TDX_BUG_ON()
   - 发件人: Huang, Kai <kai.huang@intel.com>
42. **[10-30 16:40]** Re: [PATCH v4 12/28] KVM: TDX: WARN if mirror SPTE doesn't have full
 RWX when creating S-EPT mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
43. **[10-30 23:59]** Re: [PATCH v4 12/28] KVM: TDX: WARN if mirror SPTE doesn't have full
 RWX when creating S-EPT mapping
   - 发件人: Huang, Kai <kai.huang@intel.com>
44. **[10-31 15:58]** Re: [PATCH v4 04/28] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
45. **[10-31 16:19]** Re: [PATCH v4 12/28] KVM: TDX: WARN if mirror SPTE doesn't have full
 RWX when creating S-EPT mapping
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
46. **[10-31 16:23]** Re: [PATCH v4 10/28] KVM: TDX: Fold tdx_sept_drop_private_spte()
 into tdx_sept_remove_private_spte()
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
47. **[10-31 16:26]** Re: [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
48. **[10-31 16:29]** Re: [PATCH v4 08/28] KVM: TDX: Drop superfluous page pinning in
 S-EPT management
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
49. **[10-31 16:54]** Re: [PATCH v4 16/28] KVM: TDX: ADD pages to the TD image while
 populating mirror EPT entries
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
50. **[10-31 16:54]** Re: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
51. **[10-31 16:56]** Re: [PATCH v4 17/28] KVM: TDX: Fold tdx_sept_zap_private_spte() into
 tdx_sept_remove_private_spte()
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
52. **[10-31 16:58]** Re: [PATCH v4 18/28] KVM: TDX: Combine KVM_BUG_ON + pr_tdx_error()
 into TDX_BUG_ON()
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
53. **[10-31 17:00]** Re: [PATCH v4 19/28] KVM: TDX: Derive error argument names from the
 local variable names
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
54. **[10-31 17:05]** Re: [PATCH v4 20/28] KVM: TDX: Assert that mmu_lock is held for write
 when removing S-EPT entries
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
55. **[10-31 17:08]** Re: [PATCH v4 21/28] KVM: TDX: Add macro to retry SEAMCALLs when
 forcing vCPUs out of guest
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
56. **[10-31 17:11]** Re: [PATCH v4 22/28] KVM: TDX: Add tdx_get_cmd() helper to get and
 validate sub-ioctl command
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
57. **[10-31 17:15]** Re: [PATCH v4 23/28] KVM: TDX: Convert INIT_MEM_REGION and INIT_VCPU
 to "unlocked" vCPU ioctl
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
58. **[10-31 17:17]** Re: [PATCH v4 24/28] KVM: TDX: Use guard() to acquire kvm->lock in
 tdx_vm_ioctl()
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
59. **[10-31 10:12]** Re: [PATCH v4 08/28] KVM: TDX: Drop superfluous page pinning in S-EPT management
   - 发件人: Sean Christopherson <seanjc@google.com>
60. **[10-31 17:28]** Re: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
61. **[10-31 10:34]** Re: [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 2: [PATCH RESEND v2 00/12] coc: tsm: Implement ->connect()/->disconnect() callbacks for ARM CCA IDE setup

**📧 邮件数**: 33 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 27 Oct 2025 15:25:50 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM CCA IDE 设置的补丁系列，主要实现了 TSM 的 `->connect()` 和 `->disconnect()` 回调函数。补丁的目的是为了支持 ARM CCA 的设备与 RMM 之间的通信。

**历史讨论**：
补丁系列基于之前的 TSM 框架补丁，并依赖于 KVM CCA 补丁集。补丁中提供了如何通过特定命令连接和断开设备的示例，确保了 ARM CCA IDE 的正确设置。

**本周新讨论**：
1. **补丁内容**：本周的补丁包括对 KVM 的 `kvm_has_da_feature` 函数的导出、SMCCC 驱动的管理、以及对 RMM 设备描述符的构建与注册等。
2. **进展**：参与者对补丁的细节进行了审查，提出了代码风格和结构上的改进建议，如将某些功能分离到独立的文件中，使用更具描述性的函数名等。
3. **结论**：整体上，补丁系列得到了积极的反馈，参与者认为这些改进将增强 ARM CCA 的功能和可维护性。补丁的逐步完善也显示出开发者对细节的关注和对代码质量的追求。

#### 📝 邮件列表

1. **[10-27 15:25]** [PATCH RESEND v2 00/12] coc: tsm: Implement ->connect()/->disconnect() callbacks for ARM CCA IDE setup
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[10-27 15:25]** [PATCH RESEND v2 01/12] KVM: arm64: RMI: Export kvm_has_da_feature
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[10-27 15:25]** [PATCH RESEND v2 02/12] firmware: smccc: coco: Manage arm-smccc platform device and CCA auxiliary drivers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[10-27 15:25]** [PATCH RESEND v2 03/12] coco: guest: arm64: Drop dummy RSI platform device stub
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[10-27 15:25]** [PATCH RESEND v2 04/12] coco: host: arm64: Add host TSM callback and IDE stream allocation support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[10-27 15:25]** [PATCH RESEND v2 05/12] coco: host: arm64: Build and register RMM pdev descriptors
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[10-27 15:25]** [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device communication helpers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[10-27 15:25]** [PATCH RESEND v2 07/12] coco: host: arm64: Add helper to stop and tear down an RMM pdev
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[10-27 15:25]** [PATCH RESEND v2 08/12] coco: host: arm64: Instantiate RMM pdev during device connect
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[10-27 15:25]** [PATCH RESEND v2 09/12] X.509: Make certificate parser public
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[10-27 15:26]** [PATCH RESEND v2 10/12] X.509: Parse Subject Alternative Name in certificates
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[10-27 15:26]** [PATCH RESEND v2 11/12] X.509: Move certificate length retrieval into new helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[10-27 15:26]** [PATCH RESEND v2 12/12] coco: host: arm64: Register device public key with RMM
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
14. **[10-29 16:39]** Re: [PATCH RESEND v2 01/12] KVM: arm64: RMI: Export
 kvm_has_da_feature
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
15. **[10-29 16:52]** Re: [PATCH RESEND v2 02/12] firmware: smccc: coco: Manage arm-smccc
 platform device and CCA auxiliary drivers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
16. **[10-29 16:54]** Re: [PATCH RESEND v2 03/12] coco: guest: arm64: Drop dummy RSI
 platform device stub
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
17. **[10-29 17:18]** Re: [PATCH RESEND v2 04/12] coco: host: arm64: Add host TSM
 callback and IDE stream allocation support
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
18. **[10-29 14:19]** Re: [PATCH RESEND v2 12/12] coco: host: arm64: Register device
 public key with RMM
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
19. **[10-29 17:37]** Re: [PATCH RESEND v2 05/12] coco: host: arm64: Build and register
 RMM pdev descriptors
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
20. **[10-29 18:33]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
21. **[10-29 18:34]** Re: [PATCH RESEND v2 07/12] coco: host: arm64: Add helper to stop
 and tear down an RMM pdev
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
22. **[10-29 18:38]** Re: [PATCH RESEND v2 08/12] coco: host: arm64: Instantiate RMM pdev
 during device connect
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
23. **[10-29 18:53]** Re: [PATCH RESEND v2 12/12] coco: host: arm64: Register device
 public key with RMM
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
24. **[10-30 14:14]** Re: [PATCH RESEND v2 05/12] coco: host: arm64: Build and register
 RMM pdev descriptors
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
25. **[10-30 14:48]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
26. **[10-30 10:00]** Re: [PATCH RESEND v2 05/12] coco: host: arm64: Build and register
 RMM pdev descriptors
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
27. **[10-30 10:00]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
28. **[10-30 19:34]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
29. **[10-30 21:50]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
30. **[10-30 18:02]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
31. **[10-30 18:12]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
32. **[10-31 13:34]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
33. **[10-31 12:07]** Re: [PATCH RESEND v2 06/12] coco: host: arm64: Add RMM device
 communication helpers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>

---

### Thread 3: [PATCH v3 00/25] KVM: x86/mmu: TDX post-populate cleanups

**📧 邮件数**: 31 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 16 Oct 2025 17:32:18 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（内核虚拟机）在 x86 架构下的 TDX（Trust Domain Extensions）后填充清理工作，包含 25 个补丁的第三版（PATCH v3 00/25）。

**原始补丁内容**：补丁的主要目的是清理 TDX 后填充路径，解决 KVM 内部及 gmem（guest memory）与 TDX 的后填充钩子之间的锁定问题。补丁 1 和 2 使 `kvm_arch_vcpu_async_ioctl()` 成为必需，并重命名为 `kvm_arch_vcpu_unlocked_ioctl()`。

**之前讨论要点**：历史邮件中，参与者讨论了多个补丁的具体实现及其潜在问题。例如，补丁 4 引入了一个专用 API 来映射 guest_memfd 的 pfn 到 TDP MMU，补丁 14 则在 TDH_MR_EXTEND 失败时增加了 KVM_BUG_ON() 的警告。

**本周新讨论与进展**：本周的讨论集中在补丁的细节和潜在的锁定问题上。Binbin Wu 提出是否仍需某些清理补丁，Yan Zhao 讨论了 TDX 模块的锁定行为及其与 KVM 的关系，Rick Edgecombe 提出了在 `tdh_vp_init()` 周围添加 MMU 锁的补丁，以避免在某些无故障 MMU 路径中遇到竞争。整体来看，参与者们对补丁的细节进行了深入的审查和讨论，确保了代码的稳定性和一致性。

#### 📝 邮件列表

1. **[10-16 17:32]** [PATCH v3 00/25] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-16 17:32]** [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map guest_memfd
 pfn into TDP MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-16 17:32]** [PATCH v3 13/25] KVM: TDX: Fold tdx_mem_page_record_premap_cnt() into
 its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-16 17:32]** [PATCH v3 14/25] KVM: TDX: Bug the VM if extended the initial
 measurement fails
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[10-16 17:32]** [PATCH v3 20/25] KVM: TDX: Add macro to retry SEAMCALLs when forcing
 vCPUs out of guest
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[10-16 17:32]** [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all" the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[10-22 12:53]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
8. **[10-23 22:48]** Re: [PATCH v3 14/25] KVM: TDX: Bug the VM if extended the initial
 measurement fails
   - 发件人: Huang, Kai <kai.huang@intel.com>
9. **[10-24 15:38]** Re: [PATCH v3 13/25] KVM: TDX: Fold tdx_mem_page_record_premap_cnt()
 into its sole caller
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
10. **[10-24 18:02]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
11. **[10-24 10:09]** Re: [PATCH v3 20/25] KVM: TDX: Add macro to retry SEAMCALLs when
 forcing vCPUs out of guest
   - 发件人: Huang, Kai <kai.huang@intel.com>
12. **[10-24 09:33]** Re: [PATCH v3 13/25] KVM: TDX: Fold tdx_mem_page_record_premap_cnt()
 into its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[10-24 09:35]** Re: [PATCH v3 14/25] KVM: TDX: Bug the VM if extended the initial
 measurement fails
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[10-24 09:57]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[10-27 17:01]** Re: [PATCH v3 13/25] KVM: TDX: Fold tdx_mem_page_record_premap_cnt()
 into its sole caller
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
16. **[10-27 17:26]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
17. **[10-27 17:31]** Re: [PATCH v3 14/25] KVM: TDX: Bug the VM if extended the initial
 measurement fails
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
18. **[10-27 17:46]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
19. **[10-27 11:10]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[10-27 12:20]** Re: [PATCH v3 20/25] KVM: TDX: Add macro to retry SEAMCALLs when
 forcing vCPUs out of guest
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[10-27 22:00]** Re: [PATCH v3 20/25] KVM: TDX: Add macro to retry SEAMCALLs when
 forcing vCPUs out of guest
   - 发件人: Huang, Kai <kai.huang@intel.com>
22. **[10-28 00:28]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Huang, Kai <kai.huang@intel.com>
23. **[10-27 17:28]** [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()
   - 发件人: Rick Edgecombe <rick.p.edgecombe@intel.com>
24. **[10-27 17:29]** Re: [PATCH v3 13/25] KVM: TDX: Fold tdx_mem_page_record_premap_cnt()
 into its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[10-27 17:37]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[10-28 01:01]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Huang, Kai <kai.huang@intel.com>
27. **[10-28 09:37]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
28. **[10-28 13:37]** Re: [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
29. **[10-28 17:40]** Re: [PATCH v3 24/25] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
30. **[10-29 14:37]** Re: [PATCH] KVM: TDX: Take MMU lock around tdh_vp_init()
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
31. **[10-30 16:34]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>

---

### Thread 4: [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property

**📧 邮件数**: 21 | **👥 参与者**: 8 | **📅 开始时间**: Mon, 27 Oct 2025 16:42:39 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 ARM 架构的 KVM（Kernel-based Virtual Machine）进行的两个补丁，主要集中在 FF-A（Firmware Framework for Arm）接口的支持和 TPM（Trusted Platform Module）设备的集成。

1. **原始补丁内容**：第一个补丁（PATCH 1/2）旨在修复当 FF-A 驱动作为内置模块时，FF-A 调用失败的问题。第二个补丁（PATCH 2/2）则添加对 FF-A v1.2 可选调用的支持，以便与使用 CRB 的 TPM 驱动集成。

2. **之前讨论要点**：在之前的讨论中，参与者们关注如何处理 FF-A 调用的失败情况，特别是在内置驱动的初始化顺序问题上。讨论涉及到如何确保 KVM 和 FF-A 驱动的初始化顺序，以避免在调用过程中出现不一致的状态。

3. **本周的新讨论和进展**：本周的讨论主要集中在如何优化补丁的实现。一些参与者提出应将 FF-A 调用的支持逻辑简化，避免不必要的额外调用。同时，Yeoreum Yun 提到将根据其他补丁的进展对当前补丁进行重构。此外，Per Larsen 提出了对 FF-A 消息直接请求的支持，认为这是实现 TPM 驱动的关键。最终，参与者们达成共识，认为需要进一步讨论和测试这些补丁，以确保它们在实际应用中的有效性和稳定性。

#### 📝 邮件列表

1. **[10-27 16:42]** Re: [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
2. **[10-27 19:17]** [PATCH 0/2] use TPM device with CRB over FF-A when kernel boot with pkvm
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[10-27 19:17]** [PATCH 1/2] KVM: arm64: fix FF-A call failure when ff-a driver is built-in
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[10-27 19:17]** [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[10-28 10:26]** Re: [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[10-28 12:00]** Re: [PATCH 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
7. **[10-28 21:06]** Re: [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[10-29 09:49]** Re: [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[10-29 13:36]** Re: [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[10-30 12:29]** [PATCH 0/2] KVM: arm64: Support FF-A direct messaging interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
11. **[10-30 12:29]** [PATCH 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
12. **[10-30 12:29]** [PATCH 2/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
13. **[10-30 14:29]** Re: [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Per Larsen <perl@immunant.com>
14. **[10-30 13:43]** Re: [PATCH 2/2] KVM: arm64: support optional calls of FF-A v1.2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
15. **[10-30 13:48]** Re: [PATCH 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
16. **[10-30 17:18]** Re: [PATCH 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen <perl@immunant.com>
17. **[10-30 16:52]** Re: [PATCH 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
18. **[10-31 08:09]** Re: [PATCH 1/2] KVM: arm64: fix FF-A call failure when ff-a driver
 is built-in
   - 发件人: Sebastian Ene <sebastianene@google.com>
19. **[10-31 10:08]** Re: [PATCH 1/2] KVM: arm64: fix FF-A call failure when ff-a driver
 is built-in
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
20. **[10-31 10:27]** Re: [PATCH 1/2] KVM: arm64: fix FF-A call failure when ff-a driver is built-in
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[10-31 11:11]** Re: [PATCH 1/2] KVM: arm64: fix FF-A call failure when ff-a driver
 is built-in
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 5: [PATCH 01/12] KVM: arm64: RMI: Export kvm_has_da_feature

**📧 邮件数**: 18 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 27 Oct 2025 15:18:52 +0530

#### 🤖 AI 总结

本邮件线程讨论了多个与 KVM 和 ARM CCA 相关的补丁，主要集中在 RMI（Realm Management Interface）和 TSM（Trusted Security Module）功能的实现上。

1. **原始补丁内容**：
   - 第一个补丁（PATCH 01/12）提出了导出 `kvm_has_da_feature` 函数，以便在后续补丁中使用。

2. **历史讨论要点**：
   - 之前的讨论围绕如何在 KVM 中实现 ARM CCA 的 IDE（I/O Device Emulation）设置，涉及到 SMCCC（ARM Secure Monitor Call Convention）和 RMI 设备的管理。
   - 讨论中提到需要为 ARM CCA 设备创建合适的驱动程序，并确保与 RMM（Realm Management Monitor）的通信。

3. **本周的新讨论和进展**：
   - 本周的邮件中，Aneesh Kumar K.V 提出了多个补丁，涵盖了 RMI 设备的创建、TSM 回调的注册、设备公钥的管理等。
   - 具体补丁包括：
     - 注册 RMM 设备的公钥（PATCH 12/12），以支持设备认证。
     - 解析证书链并设置公钥（PATCH 11/12）。
     - 实现 TSM 的连接和断开回调（PATCH v2 00/12），以支持 ARM CCA IDE 设置。
   - 讨论中还提到了一些关于 X.509 证书解析的补丁，旨在增强对设备认证的支持。

总体而言，本周的讨论集中在实现 ARM CCA 的功能上，特别是如何通过 RMI 和 TSM 进行设备管理和认证。

#### 📝 邮件列表

1. **[10-27 15:18]** [PATCH 01/12] KVM: arm64: RMI: Export kvm_has_da_feature
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[10-27 15:18]** [PATCH 02/12] firmware: smccc: coco: Manage arm-smccc platform device and CCA auxiliary drivers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
3. **[10-27 15:18]** [PATCH 03/12] coco: guest: arm64: Drop dummy RSI platform device stub
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
4. **[10-27 15:18]** [PATCH 04/12] coco: host: arm64: Add host TSM callback and IDE stream allocation support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
5. **[10-27 15:18]** [PATCH 05/12] coco: host: arm64: Build and register RMM pdev descriptors
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
6. **[10-27 15:18]** [PATCH 06/12] coco: host: arm64: Add RMM device communication helpers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
7. **[10-27 15:18]** [PATCH 07/12] coco: host: arm64: Add helper to stop and tear down an RMM pdev
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
8. **[10-27 15:18]** [PATCH 08/12] coco: host: arm64: Instantiate RMM pdev during device connect
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
9. **[10-27 15:19]** [PATCH 09/12] X.509: Make certificate parser public
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
10. **[10-27 15:19]** [PATCH 10/12] X.509: Parse Subject Alternative Name in certificates
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
11. **[10-27 15:19]** [PATCH 11/12] X.509: Move certificate length retrieval into new helper
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
12. **[10-27 15:19]** [PATCH 12/12] coco: host: arm64: Register device public key with RMM
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
13. **[10-27 15:19]** [PATCH v2 00/12] coc: tsm: Implement ->connect()/->disconnect() callbacks for ARM CCA IDE setup
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
14. **[10-27 15:19]** [PATCH v2 01/12] KVM: arm64: RMI: Export kvm_has_da_feature
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
15. **[10-27 15:19]** [PATCH v2 02/12] firmware: smccc: coco: Manage arm-smccc platform device and CCA auxiliary drivers
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
16. **[10-27 15:19]** [PATCH v2 03/12] coco: guest: arm64: Drop dummy RSI platform device stub
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
17. **[10-27 15:19]** [PATCH v2 04/12] coco: host: arm64: Add host TSM callback and IDE stream allocation support
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
18. **[10-27 15:33]** Re: [PATCH 01/12] KVM: arm64: RMI: Export kvm_has_da_feature
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>

---

### Thread 6: [PATCH 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC

**📧 邮件数**: 15 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 13 Oct 2025 09:32:04 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（内核虚拟机）在 arm64 架构下对 ID_PFR1_EL1.GIC 寄存器处理的修复。原始的补丁（PATCH 0/3）由 Marc Zyngier 提出，目的是解决 Peter 报告的 GICv2 虚拟机恢复失败的问题，指出 ID_PFR1_EL1.GIC 寄存器不可写，而其 64 位等效寄存器是可写的。补丁系列中，第一项补丁将 ID_PFR1_EL1.GIC 设置为可写，以解决此问题。

在历史讨论中，Marc Zyngier 提到修复 ID 寄存器在运行时的处理并不理想，建议在创建 GIC 时进行调整。Oliver Upton 也表示支持让用户空间写入 32 位 ID 寄存器的值，认为这不会影响 KVM 的功能。

本周的新讨论中，Oliver 和 Ben Horgan 继续讨论自测试的改进，Oliver 建议将某些测试中的 ksft_* 结构移除，认为其对测试的贡献不大。Mark Brown 提出了改进自测试诊断信息的补丁，增加了对寄存器读取和重置测试的详细报告，以便更清晰地识别测试失败的寄存器。整体上，本周的讨论集中在自测试的优化和补丁的细节调整上，未见重大争议。

#### 📝 邮件列表

1. **[10-13 09:32]** [PATCH 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-13 09:32]** [PATCH 1/3] KVM: arm64: Make ID_PFR1_EL1.GIC writable
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[10-14 11:21]** [PATCH 0/3] set_id_regs cleanup
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[10-14 11:21]** [PATCH 1/3] KVM: arm64: selftests: Count test_guest_reg_read() as a test
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[10-14 11:21]** [PATCH 2/3] KVM: arm64: selftests: Remove ARM64_FEATURE_FIELD_BITS and its last user
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[10-22 00:00]** Re: [PATCH 1/3] KVM: arm64: Make ID_PFR1_EL1.GIC writable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[10-29 13:45]** Re: [PATCH 2/3] KVM: arm64: selftests: Remove
 ARM64_FEATURE_FIELD_BITS and its last user
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[10-29 13:48]** Re: [PATCH 1/3] KVM: arm64: selftests: Count test_guest_reg_read()
 as a test
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[10-30 09:36]** Re: [PATCH 1/3] KVM: arm64: selftests: Count test_guest_reg_read() as
 a test
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[10-30 09:40]** Re: [PATCH 2/3] KVM: arm64: selftests: Remove
 ARM64_FEATURE_FIELD_BITS and its last user
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[10-30 11:25]** Re: [PATCH 1/3] KVM: arm64: Make ID_PFR1_EL1.GIC writable
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[10-30 15:42]** [PATCH 0/3] KVM: selftests: arm64: Improve diagnostics from
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[10-30 15:42]** [PATCH 1/3] KVM: selftests: arm64: Report set_id_reg reads of test
 registers as tests
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[10-30 15:42]** [PATCH 2/3] KVM: selftests: arm64: Report register reset tests
 individually
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[10-30 15:42]** [PATCH 3/3] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 7: [PATCH v2 0/4] KVM ARM64 pre_fault_memory

**📧 邮件数**: 11 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 13 Oct 2025 16:14:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM ARM64 的一个补丁系列，主要是增加对 KVM_PRE_FAULT_MEMORY 特性的支持，以减少执行过程中的 stage-2 故障，特别是在内存密集型应用的后复制迁移场景中。

**历史讨论**中，Jack Thomson 提出了该补丁系列的背景和目的，强调了在 ARM64 上实现此功能的重要性。补丁的第一部分实现了 KVM_PRE_FAULT_MEMORY ioctl 的支持，后续补丁则涉及修复自测试中的内存对齐问题。

**本周新讨论**中，Jack Thomson 对之前的补丁进行了回复，确认了在内存对齐不正确的情况下，munmap() 会失败。此外，Jim Mattson 提出了新的补丁，增加了对 5 级分页的支持，并修复了与 L1 和 L2 虚拟机状态相关的回归测试。具体而言，Jim 提出了四个补丁，分别是使用循环创建和遍历页表、修改虚拟机模式以支持 57 位地址，以及添加一个新的 VMX 测试以验证 KVM 对嵌套状态的保存和恢复能力。

总体来看，本周的讨论集中在补丁的审查和改进上，参与者们积极反馈并推动了补丁的完善。

#### 📝 邮件列表

1. **[10-13 16:14]** [PATCH v2 0/4] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[10-13 16:14]** [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[10-23 10:16]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-28 11:44]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
5. **[10-28 15:30]** [PATCH v2 0/4] KVM: selftests: Test SET_NESTED_STATE with 48-bit L2
 on 57-bit L1
   - 发件人: Jim Mattson <jmattson@google.com>
6. **[10-28 15:30]** [PATCH v2 1/4] KVM: selftests: Use a loop to create guest page tables
   - 发件人: Jim Mattson <jmattson@google.com>
7. **[10-28 15:30]** [PATCH v2 2/4] KVM: selftests: Use a loop to walk guest page tables
   - 发件人: Jim Mattson <jmattson@google.com>
8. **[10-28 15:30]** [PATCH v2 3/4] KVM: selftests: Change VM_MODE_PXXV48_4K to VM_MODE_PXXVYY_4K
   - 发件人: Jim Mattson <jmattson@google.com>
9. **[10-28 15:30]** [PATCH v2 4/4] KVM: selftests: Add a VMX test for LA57 nested state
   - 发件人: Jim Mattson <jmattson@google.com>
10. **[10-30 23:31]** Re: [PATCH v2 1/4] KVM: selftests: Use a loop to create guest page
 tables
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>
11. **[10-30 23:32]** Re: [PATCH v2 2/4] KVM: selftests: Use a loop to walk guest page
 tables
   - 发件人: Yosry Ahmed <yosry.ahmed@linux.dev>

---

### Thread 8: [PATCH v1 0/4] KVM: arm64: Prevent sysreg helper parameter transposition

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 27 Oct 2025 11:39:39 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM/arm64 中 sysreg 辅助函数参数转置问题的补丁系列。Fuad Tabba 提出了四个补丁，旨在通过改进参数顺序和增加编译时检查来防止参数转置错误。

首先，补丁的核心问题是 `vcpu_write_sys_reg()` 和 `__vcpu_assign_sys_reg()` 等函数在参数顺序上不一致，容易导致参数转置错误。为了解决这个问题，补丁将 `vcpu_write_sys_reg()` 的参数顺序从 `(vcpu, val, reg)` 改为 `(vcpu, reg, val)`，并增加了编译时检查，确保 `reg` 参数不能是 `u64` 类型，从而直接捕捉到转置错误。

在本周的讨论中，参与者对补丁进行了反馈。Marc Zyngier 建议在内部函数 `__vcpu_*_sys_reg()` 中也进行相应的参数顺序调整，以保持一致性。Fuad 同意这一点，并表示会在后续版本中进行修改。此外，Marc 提出了将寄存器标识符重构为结构体，以增强类型安全性，Fuad 也对此表示赞同，但认为这可能会导致较大的代码变动。

总体而言，本周的讨论集中在如何有效地实现参数检查和保持代码一致性上，补丁的目标是提高 KVM/arm64 的稳定性和安全性。

#### 📝 邮件列表

1. **[10-27 11:39]** [PATCH v1 0/4] KVM: arm64: Prevent sysreg helper parameter transposition
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[10-27 11:39]** [PATCH v1 1/4] KVM: arm64: Switch reg and val parameter ordering in vcpu_write_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[10-27 11:39]** [PATCH v1 2/4] KVM: arm64: Add compile-time type check for register
 in __vcpu_assign_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[10-27 11:39]** [PATCH v1 3/4] KVM: arm64: Add compile-time type check to vcpu_write_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[10-27 11:39]** [PATCH v1 4/4] KVM: arm64: Add compile-time type check for register
 in __vcpu_rmw_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[10-28 10:38]** Re: [PATCH v1 1/4] KVM: arm64: Switch reg and val parameter ordering in vcpu_write_sys_reg()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[10-28 10:40]** Re: [PATCH v1 1/4] KVM: arm64: Switch reg and val parameter ordering
 in vcpu_write_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[10-28 10:51]** Re: [PATCH v1 2/4] KVM: arm64: Add compile-time type check for register in __vcpu_assign_sys_reg()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[10-28 10:58]** Re: [PATCH v1 2/4] KVM: arm64: Add compile-time type check for
 register in __vcpu_assign_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[10-28 17:05]** Re: [PATCH v1 2/4] KVM: arm64: Add compile-time type check for
 register in __vcpu_assign_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[10-30 09:53]** Re: [PATCH v1 2/4] KVM: arm64: Add compile-time type check for
 register in __vcpu_assign_sys_reg()
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 9: [PATCH v2 0/2] use TPM device with CRB over FF-A when kernel boot with pkvm

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 30 Oct 2025 10:22:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在使用 PKVM 启动内核时，如何通过 FF-A 使用 TPM 设备。Yeoreum Yun 提出了一个补丁系列（PATCH v2 0/2），旨在解决在 kvm-arm.mode=protected 模式下，内核启动时 TPM 设备探测失败的问题。补丁建议将 CONFIG_ARM_FFA_TRANSPORT 和 CONFIG_TCG_ARM_CRB_FFA 作为内置选项编译，以便与 IMA 子系统集成，从而生成包含 PCR 值的 boot_aggregate 日志。

在之前的讨论中，Yeoreum 提到，当 FF-A 驱动作为模块构建时，FF-A 函数调用正常，但若作为内置驱动，所有 FF-A 调用将失败。为了解决这个问题，补丁修改了 FF-A 驱动的初始化顺序，确保在内核启动时能够正确设置版本协商标志。

本周的讨论中，Yeoreum 提交了两个补丁，分别修复了 FF-A 调用失败的问题，并支持 FF-A v1.2 的一些可选调用。Per Larsen 也参与了讨论，提出了对 FF-A 直接消息接口的支持，确保与 TPM 驱动的兼容性。整体来看，补丁系列得到了积极的反馈，Yeoreum 表示对该系列的满意，并进行了审核。

#### 📝 邮件列表

1. **[10-30 10:22]** [PATCH v2 0/2] use TPM device with CRB over FF-A when kernel boot with pkvm
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[10-30 10:22]** [PATCH v2 1/2] KVM: arm64: fix FF-A call failure when ff-a driver is built-in
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[10-30 10:22]** [PATCH v2 2/2] KVM: arm64: support some optional calls of FF-A v1.2
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[10-30 15:49]** [PATCH v2 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[10-30 15:49]** [PATCH v2 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[10-30 15:49]** [PATCH v2 2/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[10-30 17:59]** [PATCH v2 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
8. **[10-30 17:59]** [PATCH v2 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
9. **[10-30 17:59]** [PATCH v2 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
10. **[10-30 20:28]** Re: [PATCH v2 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 10: [PATCH V2 0/2] arm64/mm: Add remaining TLBI_XXX_MASK macros

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 24 Oct 2025 05:02:05 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 ARM64 架构的内存管理，提出的补丁（patch）旨在添加剩余的 TLBI_XXX_MASK 宏。补丁的主要内容包括去掉冗余的级别修剪操作，并将 TLBI_TTL_MASK 拆分为 TLBI_TTL_MASK 和 TLBI_TG_MASK，以便更清晰地表示页面大小和页表级别信息。

在历史讨论中，参与者对补丁进行了初步审查，Ben Horgan 表示代码看起来正确，但对 TTL 拆分的合理性表示不确定。Jonathan Cameron 提出了使用 FIELD_MODIFY 宏的建议，以减少代码冗余。

在本周的新讨论中，Anshuman Khandual 强调了补丁的设计意图，即在最小化 KVM 代码变更的同时适应掩码的拆分。Jonathan Cameron 继续探讨 FIELD_MODIFY 宏的使用，认为在某些情况下可能合适，但会增加代码变动。整体来看，讨论围绕补丁的实现细节和潜在的代码优化展开，尚未达成最终结论。

#### 📝 邮件列表

1. **[10-24 05:02]** [PATCH V2 0/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[10-24 05:02]** [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[10-24 09:56]** Re: [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[10-24 12:00]** Re: [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
5. **[10-27 06:44]** Re: [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[10-27 07:06]** Re: [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
7. **[10-28 12:43]** Re: [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
8. **[10-30 08:11]** Re: [PATCH V2 2/2] arm64/mm: Add remaining TLBI_XXX_MASK macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 11: [PATCH v9 0/5] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 29 Oct 2025 15:46:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.8 SPE 特性的补丁集（[PATCH v9 0/5]），主要集中在数据源过滤功能的支持上。补丁的核心是引入了一个新的配置字段 `config4`，以便在性能事件中实现数据源过滤（SPE_FEAT_FDS）。

在历史讨论中，补丁经历了多个版本的迭代，逐步修正了文档中的错误，优化了代码结构，并解决了与其他功能的冲突。补丁的主要变更包括：在 `perf_event_attr` 结构中添加 `config4` 字段，支持通过 `inv_data_src_filter` 进行数据源过滤，并在文档中详细描述了新特性。

本周的新讨论中，James Clark 提交了补丁的最新版本，强调了对数据源过滤的支持和文档更新。补丁得到了多位开发者的审核和测试，确保了新功能的稳定性和兼容性。此外，文档中详细说明了如何使用新特性，包括如何通过设置 `inv_data_src_filter` 来排除特定的数据源。

总的来说，这一系列补丁旨在增强 ARM SPE 的性能监控能力，使其能够更灵活地处理数据源过滤，从而提升性能分析的准确性和效率。

#### 📝 邮件列表

1. **[10-29 15:46]** [PATCH v9 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[10-29 15:46]** [PATCH v9 1/5] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
3. **[10-29 15:46]** [PATCH v9 2/5] perf: arm_spe: Add support for filtering on data
 source
   - 发件人: James Clark <james.clark@linaro.org>
4. **[10-29 15:46]** [PATCH v9 3/5] tools headers UAPI: Sync linux/perf_event.h with
 the kernel sources
   - 发件人: James Clark <james.clark@linaro.org>
5. **[10-29 15:46]** [PATCH v9 4/5] perf tools: Add support for
 perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
6. **[10-29 15:46]** [PATCH v9 5/5] perf docs: arm-spe: Document new SPE filtering
 features
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 12: [PATCH v6 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 24 Oct 2025 17:08:12 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.7 架构新增的 FEAT_{LS64, LS64_V} 特性的支持及相关测试的补丁（PATCH v6 0/7）。该补丁的主要内容包括：在 CPU 特性列表中添加识别和启用这些特性，向用户空间暴露支持信息，通过 HWCAP3 和 cpuinfo 进行展示，增加相关的硬件能力测试，并处理虚拟机中对不支持内存访问的异常。

在历史讨论中，Zhou Wang 提出了补丁的初步实现，并讨论了如何处理在测试中可能出现的 SIGILL 和 SIGBUS 异常。Arnd Bergmann 提出了一些关于汇编代码的改进建议，特别是关于寄存器的使用和异常处理的细节。

在本周的新讨论中，Zhou Wang 纠正了自己之前对异常处理的理解，明确指出在访问不支持的内存类型时应触发数据中止，而不是返回特定的寄存器值。Arnd Bergmann 也承认了之前的误解，并表示将进一步修改测试代码以符合 ARM 规范的要求。整体来看，讨论集中在如何准确实现和测试新特性，以确保系统的稳定性和可靠性。

#### 📝 邮件列表

1. **[10-24 17:08]** [PATCH v6 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[10-24 17:08]** [PATCH v6 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[10-24 18:18]** Re: [PATCH v6 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
4. **[10-25 18:06]** Re: [PATCH v6 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64,
 LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
5. **[10-27 10:50]** Re: [PATCH v6 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64,
 LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[10-27 07:57]** Re: [PATCH v6 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>

---

### Thread 13: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 30 Oct 2025 16:05:05 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中的一个补丁，旨在为 `guest_memfd` 添加一个模块参数，以禁用 TLB（Translation Lookaside Buffer）刷新。补丁的主要目的是优化内存管理，特别是在处理虚拟机内存时。

在历史讨论中，虽然没有具体的历史邮件，但可以推测出补丁的背景涉及对内存映射和分配机制的改进，尤其是在处理直接映射时的挑战。

本周的新讨论中，Brendan Jackman 提出了一个建议，介绍了一种新的内存分配逻辑，称为“freetype”，该逻辑可以在分配内存时有效地管理页面块，减少 TLB 刷新的需求。他指出，尽管当前的补丁可能对 Firecracker 等特定用例不适用，但仍然值得合并，因为它对其他用户是有价值的。此外，他还讨论了在内存分配过程中可能出现的递归问题，并提出了一些解决方案，包括在检测到递归时失败映射路径的建议。

总体来看，本周的讨论集中在补丁的实现细节和潜在问题上，参与者们积极探索如何优化 KVM 的内存管理功能。

#### 📝 邮件列表

1. **[10-30 16:05]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Brendan Jackman <jackmanb@google.com>
2. **[10-30 17:18]** Re: [PATCH v7 12/12] KVM: selftests: Test guest execution from direct
 map removed gmem
   - 发件人: Brendan Jackman <jackmanb@google.com>
3. **[10-31 17:30]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
4. **[10-31 18:31]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Brendan Jackman <jackmanb@google.com>
5. **[11-01 11:39]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>

---

### Thread 14: [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory share

**📧 邮件数**: 5 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 17 Oct 2025 07:57:10 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下检查 FF-A（Firmware Framework for Arm）内存共享中的不可信偏移量的补丁。

1. **原始补丁内容**：Sebastian Ene 提出的补丁旨在验证 FF-A 缓冲区的偏移量，以防止在 hypervisor 中发生越界访问。补丁通过检查从主机内核传递的偏移量，确保其不会超出有效范围。

2. **之前讨论要点**：在历史讨论中，Vincent Donnefort 提到该补丁的安全性问题，认为即使是简单的读取操作也可能导致系统崩溃。他建议将偏移量检查与范围数量的检查结合起来，以便更清晰地处理潜在的安全漏洞。

3. **本周新讨论与进展**：本周的讨论中，Sebastian Ene 进一步阐述了潜在的攻击路径，指出如果偏移量溢出，攻击者可能利用这一点进行“混淆代理攻击”。Will Deacon 对补丁表示认可，认为其解决了问题，并给予了支持。最后，Marc Zyngier 确认该补丁已被应用到修复中，标志着讨论的圆满结束。

总体来看，该补丁通过增强对不可信偏移量的检查，提高了 KVM 在 arm64 架构下的安全性，得到了社区成员的认可和支持。

#### 📝 邮件列表

1. **[10-17 07:57]** [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory share
   - 发件人: Sebastian Ene <sebastianene@google.com>
2. **[10-22 16:21]** Re: [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory
 share
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[10-29 10:27]** Re: [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory
 share
   - 发件人: Sebastian Ene <sebastianene@google.com>
4. **[10-29 16:23]** Re: [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory
 share
   - 发件人: Will Deacon <will@kernel.org>
5. **[10-30 16:23]** Re: [PATCH] KVM: arm64: Check the untrusted offset in FF-A memory share
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU tables

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 12 Oct 2025 23:51:25 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下优化影子 S2-MMU 表解除映射的补丁（PATCH v2）。该补丁旨在解决在解除映射时，因缺乏直接映射而导致的全地址空间遍历和无效化的问题，这在处理大页时会引发显著的性能瓶颈。

在历史讨论中，补丁的提出者 Ganapatrao Kulkarni 指出，当前的解除映射机制在处理大页时会导致大量循环迭代，严重影响性能。Marc Zyngier 对该补丁提出了批评，认为其缺乏对多重映射的处理，且没有相关文档和测试，导致其优化效果不可靠。

在本周的新讨论中，Ganapatrao Kulkarni 提出了改进建议，建议在查找时将多个映射范围添加到树节点中，以便在解除映射时逐一处理。他在测试中发现，这种方法显著降低了解除映射的延迟。然而，Marc Zyngier 对此表示质疑，认为该方法未能满足架构要求，且强调验证现有代码的必要性，认为当前的设计更多是围绕 Linux 的行为，而非架构本身的需求。

总结来看，尽管提出了优化方案，但在架构正确性和性能之间的平衡仍存在争议，后续需要更多的测试和验证以确保方案的有效性。

#### 📝 邮件列表

1. **[10-12 23:51]** [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU tables
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[10-23 16:41]** Re: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
3. **[10-23 15:35]** Re: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU tables
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[10-28 11:32]** Re: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU
 tables
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
5. **[10-28 12:29]** Re: [PATCH v2] KVM: arm64: nv: Optimize unmapping of shadow S2-MMU tables
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 16 Oct 2025 17:45:41 +0100

#### 🤖 AI 总结

在本邮件讨论中，主题为“[PATCH v3] KVM: arm64: Check range args for pKVM mem transitions”的补丁旨在解决当前在 pKVM 内存转换中缺乏对主机发起的范围参数的验证问题。该补丁通过在每个公共函数中增加 pfn_range_is_valid() 检查，来防止可能的溢出和后续检查的绕过。此外，补丁提到，host_unshare_guest 转换已经通过 __check_host_shared_guest() 进行了保护。

在之前的讨论中，Vincent Donnefort 提出了补丁的背景和必要性，强调了对范围参数的检查缺失可能导致的安全隐患。

在本周的新讨论中，Sebastian Ene 认为新增的函数在没有持有主机锁的情况下调用是安全的，因为没有发现对 vtcr 字段的直接修改。他指出，__pkvm_host_share_guest 已经包含了对 nr_pages 的限制，因此不需要额外的检查。然而，Vincent Donnefort 反驳说，__guest_check_transition_size 只限制到 PMD_SIZE，这在大于 4KiB 页的系统中仍然存在漏洞，值得修复。最终，Marc Zyngier 确认该补丁已被应用并感谢参与者的贡献。

#### 📝 邮件列表

1. **[10-16 17:45]** [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[10-30 06:09]** Re: [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Sebastian Ene <sebastianene@google.com>
3. **[10-30 15:54]** Re: [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[10-30 16:23]** Re: [PATCH v3] KVM: arm64: Check range args for pKVM mem transitions
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 30 Oct 2025 12:27:04 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 ID_PFR1_EL1.GIC 的问题，主要集中在修复与 GIC（通用中断控制器）相关的寄存器处理。

**原始 patch/问题的内容**：
Marc Zyngier 提出了一个补丁系列（PATCH v2 0/3），旨在修复在 GICv2 虚拟机恢复时出现的问题。具体来说，ID_PFR1_EL1.GIC 寄存器不可写，而其 64 位等价物是可写的，这导致了 GICv2 虚拟机的恢复失败。

**之前讨论要点**：
在之前的讨论中，Peter Maydell 报告了该问题，并指出在 6.12 版本中引入的更改破坏了 GICv2 虚拟机的恢复。Marc 提到，修复 ID 寄存器的运行时处理并不是最佳方案，应该在 GIC 创建时就进行调整。

**本周的新讨论、进展或结论**：
本周的讨论中，Marc 提出了三个具体的补丁：
1. **补丁 1**：使所有 32 位 ID 寄存器完全可写，以解决 GICv2 虚拟机恢复的问题。
2. **补丁 2**：在配置 GICv3 时直接设置 ID_{AA64PFR0,PFR1}_EL1.GIC 寄存器，避免运行时清除。
3. **补丁 3**：限制 ID_{AA64PFR0,PFR1}_EL1.GIC 的清除操作，仅在用户空间 irqchip 的特殊情况下进行。

这些补丁已在 Marc 的测试环境中成功应用，使得 GICv2 虚拟机的保存和恢复功能正常工作。整体来看，此次讨论推动了对 KVM arm64 的重要修复进展。

#### 📝 邮件列表

1. **[10-30 12:27]** [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[10-30 12:27]** [PATCH v2 1/3] KVM: arm64: Make all 32bit ID registers fully writable
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[10-30 12:27]** [PATCH v2 2/3] KVM: arm64: Set ID_{AA64PFR0,PFR1}_EL1.GIC when GICv3 is configured
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[10-30 12:27]** [PATCH v2 3/3] KVM: arm64: Limit clearing of ID_{AA64PFR0,PFR1}_EL1.GIC to userspace irqchip
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 16 Oct 2025 10:28:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 中添加 NUMA mempolicy 支持的补丁（PATCH v13 00/12）。该补丁由 Shivank 提出，旨在增强 guest_memfd 的内存管理能力，以支持 NUMA-aware 的内存分配策略。

在历史讨论中，Sean Christopherson 提到该补丁系列的背景，并指出需要对 cpuset_do_page_mem_spread() 的行为进行测试，尽管他认为可以在没有这些测试的情况下合并补丁。此外，补丁 v13 还包括了对代码格式的调整和一些小错误的修复。

在本周的新讨论中，Vlastimil Babka 对补丁进行了审查，并提出了一些小建议，认为某些部分可能不必要，并询问是否与 VFS 的某些操作有关。Shivank 对这些反馈表示感谢，并确认了一个在调试过程中发现的竞争条件，涉及到 kvm_amd 模块卸载时的 gmem 支持虚拟机的行为。Shivank 还提供了相关的详细信息链接。

总体来看，本周的讨论主要集中在补丁的审查和潜在问题的确认上，参与者们对补丁的进一步改进表示积极的态度。

#### 📝 邮件列表

1. **[10-16 10:28]** [PATCH v13 00/12] KVM: guest_memfd: Add NUMA mempolicy support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-16 10:28]** [PATCH v13 04/12] KVM: guest_memfd: Add slab-allocated inode cache
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-27 12:06]** Re: [PATCH v13 04/12] KVM: guest_memfd: Add slab-allocated inode
 cache
   - 发件人: Vlastimil Babka <vbabka@suse.cz>
4. **[10-27 17:55]** Re: [PATCH v13 04/12] KVM: guest_memfd: Add slab-allocated inode
 cache
   - 发件人: Garg, Shivank <shivankg@amd.com>

---

### Thread 19: [PATCH] KVM: arm64: Use pointer from memcpy() call for assignment in
 init_hyp_mode()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 30 Oct 2025 18:11:03 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，目的是在 `init_hyp_mode()` 函数中使用 `memcpy()` 调用的返回指针进行赋值。

**原始补丁内容**：
补丁通过将 `memcpy()` 的返回值直接赋值给 `page_addr`，简化了代码。具体来说，原本的代码中先获取了 `page_address(page)` 的值，然后再调用 `memcpy()`，而补丁将这两步合并为一行。

**之前讨论要点**：
在历史讨论中并未提及，但从本周的讨论来看，补丁的提出引发了一些质疑，主要集中在代码可读性和维护性上。参与者 Mark Rutland 指出，这种修改使得代码更难以阅读和修改，并且没有实际的空间节省。

**本周的新讨论与进展**：
本周的讨论主要集中在对补丁的反对意见上。Mark Rutland 和 David Laight 都认为这个修改并不值得，尽管可能在寄存器使用上有微小的优化，但整体上并没有实质性的好处。David 进一步提到，`memcpy()` 的返回值在许多实现中并不可靠，建议将其视为 `void` 类型。整体来看，本周的讨论倾向于反对该补丁的实施。

#### 📝 邮件列表

1. **[10-30 18:11]** [PATCH] KVM: arm64: Use pointer from memcpy() call for assignment in
 init_hyp_mode()
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
2. **[10-30 17:49]** Re: [PATCH] KVM: arm64: Use pointer from memcpy() call for
 assignment in init_hyp_mode()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[10-30 21:21]** Re: [PATCH] KVM: arm64: Use pointer from memcpy() call for
 assignment in init_hyp_mode()
   - 发件人: David Laight <david.laight.linux@gmail.com>

---

### Thread 20: [PATCH] KVM: arm64: vgic-v3: Trap all if no in-kernel irqchip

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 21 Oct 2025 09:44:09 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-v3（虚拟通用中断控制器 v3）相关的一个补丁。补丁的主要内容是：当没有内核中的 irqchip 时，设置所有的陷阱位以阻止所有访问，从而修复 no-vgic-v3 的自测问题。

在历史讨论中，Sascha Bischoff 提出了这个补丁，并指出它修复了之前的一个问题，该问题与 KVM 在处理 GICv3 主机时的陷阱设置有关。补丁的修复与之前的一个提交（3193287ddffb）相关，该提交只对 v2-on-v3 或 v3 客户进行陷阱设置。

在本周的新讨论中，参与者 Sebastian Ott 对补丁进行了审核并表示认可，确认其有效性。随后，Marc Zyngier 表示该补丁已被应用到修复列表中，并感谢 Sascha 的贡献。这表明补丁得到了积极的反馈，并成功合并到代码库中。

#### 📝 邮件列表

1. **[10-21 09:44]** [PATCH] KVM: arm64: vgic-v3: Trap all if no in-kernel irqchip
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[10-27 15:02]** Re: [PATCH] KVM: arm64: vgic-v3: Trap all if no in-kernel irqchip
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[10-30 16:23]** Re: [PATCH] KVM: arm64: vgic-v3: Trap all if no in-kernel irqchip
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH] KVM: arm64: FFA: Use pointers from memcpy() calls for
 assignments in three functions

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 30 Oct 2025 18:40:39 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“使用来自 memcpy() 调用的指针进行三个函数中的赋值”。该补丁的主要目的是优化代码，通过直接将 memcpy() 的返回值赋给变量，简化了原有的赋值和内存拷贝操作。

在历史讨论中没有相关内容，但本周的讨论中，补丁的作者 Markus Elfring 提出了具体的代码修改，展示了如何将 buf 变量的赋值与 memcpy() 调用结合起来，以减少冗余代码。然而，Marc Zyngier 对此表示反对，认为这种修改使代码变得难以阅读，并且破坏了开发者依赖的模式，因此不打算接受该补丁。

总结来看，尽管补丁旨在提高代码的简洁性，但由于可读性和代码风格的考虑，目前尚未获得认可，后续可能需要进一步讨论和修改。

#### 📝 邮件列表

1. **[10-30 18:40]** [PATCH] KVM: arm64: FFA: Use pointers from memcpy() calls for
 assignments in three functions
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
2. **[10-30 18:07]** Re: [PATCH] KVM: arm64: FFA: Use pointers from memcpy() calls for assignments in three functions
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: selftests: Filter ZCR_EL2 in get-reg-list

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 24 Oct 2025 00:43:39 +0100

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH] KVM: arm64: selftests: Filter ZCR_EL2 in get-reg-list”。该补丁的主要目的是在 KVM 的 arm64 自测试中，过滤掉 ZCR_EL2 寄存器，以避免在 NV 启用但未启用 SVE 的情况下测试失败。之前的讨论指出，get-reg-list 在列出 EL2 寄存器时包含了 ZCR_EL2，但没有为该寄存器设置功能门，这导致在测试某些特性组合时会出现缺失寄存器的错误。

在本周的新讨论中，Marc Zyngier 对该补丁表示感谢，并确认已将其应用于修复列表中。补丁的提交哈希为 a186fbcfd845699d51809f7c7e54cf997fe32820。这表明该问题已得到解决，并且补丁已成功合并。整体来看，本周的进展是补丁的确认和应用，标志着对问题的有效处理。

#### 📝 邮件列表

1. **[10-24 00:43]** [PATCH] KVM: arm64: selftests: Filter ZCR_EL2 in get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[10-30 16:23]** Re: [PATCH] KVM: arm64: selftests: Filter ZCR_EL2 in get-reg-list
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 23: [PATCH] KVM: arm64: selftests: Add SCTLR2_EL2 to get-reg-list

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 23 Oct 2025 22:19:29 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 的 arm64 自测试中添加 SCTLR2_EL2 寄存器到获取寄存器列表的补丁（patch）。历史讨论中，Mark Brown 提出了该补丁，指出虽然内核已经支持 SCTLR2_EL2，但在获取寄存器列表时未将其包含，导致在可用时报告缺失。补丁通过在相关代码中添加两行代码来解决这一问题。

在本周的新讨论中，Marc Zyngier 对该补丁进行了确认，并表示已将其应用于修复列表中，感谢 Mark 的贡献。补丁的提交哈希为 92e781c93ebe75e39ecdf78fb8ef1fdf1b63a9f8。

总结而言，此次讨论的重点在于修复 KVM arm64 自测试中对 SCTLR2_EL2 寄存器的遗漏问题，补丁已成功应用，标志着该问题的解决。

#### 📝 邮件列表

1. **[10-23 22:19]** [PATCH] KVM: arm64: selftests: Add SCTLR2_EL2 to get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[10-30 16:23]** Re: [PATCH] KVM: arm64: selftests: Add SCTLR2_EL2 to get-reg-list
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH v2] KVM: selftests: fix MAPC RDbase target formatting in vgic_lpi_stress

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 20 Oct 2025 16:59:46 +0200

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 自测试的补丁，主题为修复 vgic_lpi_stress 中 MAPC RDbase 目标格式的问题。

**原始 patch/问题的内容**：
补丁由 Maximilian Dittgen 提出，主要问题在于 GITS_TYPER.PTA 为 0 时，ITS MAPC 命令要求使用 CPU ID，而非物理重分配器地址作为 RDbase 命令参数。在进行 MAPC 操作时，vgic_lpi_stress 迭代 CPU ID，并将其作为 RDbase vcpu_id 参数传递给 its_send_mapc_cmd()。然而，its_send_mapc_cmd() 自测处理程序中的 its_encode_target() 期望 RDbase 参数使用 16 位偏移格式。

**之前的讨论要点**：
在历史讨论中，补丁的背景和问题被详细阐述，强调了 MAPC 命令参数格式不匹配的问题，指出了需要修复的具体内容。

**本周的新讨论、进展或结论**：
在本周的讨论中，Marc Zyngier 确认已将该补丁应用于修复分支，并表示感谢。这表明补丁已经被接受并将被纳入后续的代码更新中。

#### 📝 邮件列表

1. **[10-20 16:59]** [PATCH v2] KVM: selftests: fix MAPC RDbase target formatting in vgic_lpi_stress
   - 发件人: Maximilian Dittgen <mdittgen@amazon.de>
2. **[10-30 16:23]** Re: [PATCH v2] KVM: selftests: fix MAPC RDbase target formatting in vgic_lpi_stress
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 25: [PATCH] arm64: Fix double word in comments

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 29 Oct 2025 15:17:42 +0800

#### 🤖 AI 总结

本邮件讨论的主题是一个针对 arm64 架构的补丁，旨在修复代码注释中的重复词汇问题。补丁由 Bo Liu 提交，主要内容是删除注释中多余的“the”一词，以提高代码的可读性和准确性。

在历史讨论中并没有相关的背景信息或先前的讨论记录，因此本周的新讨论是该补丁的唯一内容。Bo Liu 在邮件中详细说明了补丁的具体修改，包括在两个文件中的更改：`entry-ftrace.S` 和 `arm.c`，每个文件都进行了相应的注释修正。

本周的进展表明，该补丁已经完成并提交，未提及任何争议或需进一步讨论的事项，表明该修改被认为是简单且必要的。整体来看，这次讨论专注于代码质量的提升，确保注释的准确性。

#### 📝 邮件列表

1. **[10-29 15:17]** [PATCH] arm64: Fix double word in comments
   - 发件人: Bo Liu <liubo03@inspur.com>

---

## 📌 Bug Report

共 2 个 thread

---

### Thread 1: Failing no-vgic-v3 test

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 27 Oct 2025 12:37:54 +0100 (CET)

#### 🤖 AI 总结

本邮件讨论的主题是关于在无 VGICv3 的环境下进行自测时出现的失败问题。Sebastian Ott 提到在 Ampere Altra 处理器上运行 `no-vgic-v3` 测试时，出现了断言失败，具体错误信息显示在访问寄存器时未能触发预期的未定义异常（UNDEF）。他指出，这与之前的补丁有关，该补丁限制了对 GICv3 硬件的某些访问。

在历史讨论中，Sebastian 提出了一个本地修复方案，修改了 `vgic-v3.c` 文件中的条件判断，以确保在没有内核 VGIC 的情况下，能够正确处理 GICv3 兼容主机的寄存器访问。

本周的新讨论中，Sascha Bischoff 对 Sebastian 的问题进行了回应，承认之前的补丁未考虑到在某些情况下可能不会创建内核 VGIC。他提供了一个修复方案，并请求 Sebastian 测试该修复。Sebastian 随后确认该修复有效，解决了测试失败的问题。

总结而言，此次讨论围绕无 VGICv3 测试失败的原因及其修复展开，最终通过修复补丁解决了问题。

#### 📝 邮件列表

1. **[10-27 12:37]** Failing no-vgic-v3 test
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[10-27 12:01]** Re: Failing no-vgic-v3 test
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[10-27 13:17]** Re: Failing no-vgic-v3 test
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 2: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 29 Oct 2025 13:04:27 -0700

#### 🤖 AI 总结

本邮件线程讨论了在 KVM ARM 虚拟化环境中出现的一个内核错误，具体是 `kvm_s2_put_page` 函数中的 bug。该问题由 syzbot 提出，报告了在特定条件下触发的内核错误，涉及到页面引用计数为零的情况，导致系统崩溃。

在历史讨论中，并没有提供具体的补丁或详细的背景信息，但可以看出该问题的严重性，影响了虚拟化的稳定性。

在本周的新讨论中，syzbot 提供了一个可重现的测试用例，并附上了相关的调试信息和内核配置。接着，开发者 Oliver Upton 提出了解决方案，建议撤销之前的一个补丁，即“在销毁阶段-2 页表时按需重新调度”。他已经将 KVM ARM 的代码库更新到包含该修复的版本 6.18-rc3，以解决此问题。

总的来说，本周的讨论集中在确认问题的存在和提出解决方案上，开发者们积极响应并推进了修复进程。

#### 📝 邮件列表

1. **[10-29 13:04]** Re: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page
   - 发件人: syzbot <syzbot+c41f3ddb8299a30a98b5@syzkaller.appspotmail.com>
2. **[10-29 13:27]** Re: [syzbot] [kvmarm?] kernel BUG in kvm_s2_put_page
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

