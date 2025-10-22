# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:41:53

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 272
- **总 Thread 数**: 23
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 20 threads (262 邮件)
- **RFC**: 1 threads (1 邮件)
- **Bug Report**: 1 threads (7 邮件)
- **GIT PULL**: 1 threads (2 邮件)

---

## 📌 PATCH

共 20 个 thread

---

### Thread 1: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support

**📧 邮件数**: 72 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 11 Jun 2025 15:45:03 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）的多个补丁，主要集中在对设备发布中断（posted IRQs）和 IOMMU（输入输出内存管理单元）支持的改进。

**1. 原始补丁/问题内容：**
补丁系列的主题是对 KVM 中设备发布中断支持的全面改进，特别是针对 AMD 处理器的 SVM（安全虚拟机）实现。补丁旨在修复与设备发布中断相关的多种错误，并清理 KVM 的实现。

**2. 之前讨论要点：**
历史讨论中提到，补丁系列的第一部分包含了针对 arm64 的修复，其他补丁则主要集中在 SVM 特定的改进上。补丁还涉及到对 IRQ 路由的更新逻辑进行简化，以避免不必要的复杂性和潜在的错误。

**3. 本周的新讨论、进展或结论：**
本周的讨论集中在补丁的具体实现和改进上，包括：
- 增强了对 IRQ 路由更新的处理，避免在没有目标 vCPU 的情况下进行不必要的更新。
- 引入了新的机制来控制 GA 日志中断的生成，确保只有在 vCPU 阻塞时才会生成这些中断。
- 讨论了在更新 IRTE 时如何处理与 IOMMU 相关的元数据，确保在 AVIC 被禁用时仍能正确更新 IRTE。
- 参与者对补丁提出了多项建议和改进意见，确保代码的可读性和维护性。

总的来说，本周的讨论推动了 KVM 对设备发布中断支持的进一步完善，确保了在不同架构上的一致性和稳定性。

#### 📝 邮件列表

1. **[06-11 15:45]** [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-11 15:45]** [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type
 changes as changes
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-11 15:45]** [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-11 15:45]** [PATCH v3 03/62] KVM: Pass new routing entries and irqfd when
 updating IRTEs
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-11 15:45]** [PATCH v3 04/62] KVM: SVM: Track per-vCPU IRTEs using
 kvm_kernel_irqfd structure
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-11 15:45]** [PATCH v3 05/62] KVM: SVM: Delete IRTE link from previous vCPU before
 setting new IRTE
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-11 15:45]** [PATCH v3 06/62] iommu/amd: KVM: SVM: Delete now-unused
 cached/previous GA tag fields
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-11 15:45]** [PATCH v3 07/62] KVM: SVM: Delete IRTE link from previous vCPU
 irrespective of new routing
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[06-11 15:45]** [PATCH v3 08/62] KVM: SVM: Drop pointless masking of default APIC
 base when setting V_APIC_BAR
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-11 15:45]** [PATCH v3 09/62] KVM: SVM: Drop pointless masking of kernel page pa's
 with AVIC HPA masks
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[06-11 15:45]** [PATCH v3 10/62] KVM: SVM: Add helper to deduplicate code for getting
 AVIC backing page
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[06-11 15:45]** [PATCH v3 11/62] KVM: SVM: Drop vcpu_svm's pointless
 avic_backing_page field
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[06-11 15:45]** [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead of
 rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[06-11 15:45]** [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on ID
 during vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[06-11 15:45]** [PATCH v3 14/62] KVM: SVM: Track AVIC tables as natively sized
 pointers, not "struct pages"
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[06-11 15:45]** [PATCH v3 15/62] KVM: SVM: Drop superfluous "cache" of AVIC Physical
 ID entry pointer
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[06-11 15:45]** [PATCH v3 16/62] KVM: VMX: Move enable_ipiv knob to common x86
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[06-11 15:45]** [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set IsRunning
 if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[06-11 15:45]** [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization if CPU
 has erratum #1235
   - 发件人: Sean Christopherson <seanjc@google.com>
20. **[06-11 15:45]** [PATCH v3 19/62] KVM: VMX: Suppress PI notifications whenever the
 vCPU is put
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[06-11 15:45]** [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[06-11 15:45]** [PATCH v3 21/62] iommu/amd: KVM: SVM: Use pi_desc_addr to derive ga_root_ptr
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[06-11 15:45]** [PATCH v3 22/62] iommu/amd: KVM: SVM: Pass NULL @vcpu_info to
 indicate "not guest mode"
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[06-11 15:45]** [PATCH v3 23/62] KVM: SVM: Stop walking list of routing table entries
 when updating IRTE
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[06-11 15:45]** [PATCH v3 24/62] KVM: VMX: Stop walking list of routing table entries
 when updating IRTE
   - 发件人: Sean Christopherson <seanjc@google.com>
26. **[06-11 15:45]** [PATCH v3 25/62] KVM: SVM: Extract SVM specific code out of get_pi_vcpu_info()
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[06-11 15:45]** [PATCH v3 26/62] KVM: x86: Move IRQ routing/delivery APIs from x86.c
 => irq.c
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-11 15:45]** [PATCH v3 27/62] KVM: x86: Nullify irqfd->producer after updating IRTEs
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[06-11 15:45]** [PATCH v3 28/62] KVM: x86: Dedup AVIC vs. PI code for identifying
 target vCPU
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[06-11 15:45]** [PATCH v3 29/62] KVM: x86: Move posted interrupt tracepoint to common code
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[06-11 15:45]** [PATCH v3 30/62] KVM: SVM: Clean up return handling in avic_pi_update_irte()
   - 发件人: Sean Christopherson <seanjc@google.com>
32. **[06-11 15:45]** [PATCH v3 31/62] iommu: KVM: Split "struct vcpu_data" into separate
 AMD vs. Intel structs
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[06-11 15:45]** [PATCH v3 32/62] KVM: Don't WARN if updating IRQ bypass route fails
   - 发件人: Sean Christopherson <seanjc@google.com>
34. **[06-11 15:45]** [PATCH v3 33/62] KVM: Fold kvm_arch_irqfd_route_changed() into kvm_arch_update_irqfd_routing()
   - 发件人: Sean Christopherson <seanjc@google.com>
35. **[06-11 15:45]** [PATCH v3 34/62] KVM: x86: Track irq_bypass_vcpu in common x86 code
   - 发件人: Sean Christopherson <seanjc@google.com>
36. **[06-11 15:45]** [PATCH v3 35/62] KVM: x86: Skip IOMMU IRTE updates if there's no old
 or new vCPU being targeted
   - 发件人: Sean Christopherson <seanjc@google.com>
37. **[06-11 15:45]** [PATCH v3 36/62] KVM: x86: Don't update IRTE entries when old and new
 routes were !MSI
   - 发件人: Sean Christopherson <seanjc@google.com>
38. **[06-11 15:45]** [PATCH v3 37/62] KVM: SVM: Revert IRTE to legacy mode if IOMMU
 doesn't provide IR metadata
   - 发件人: Sean Christopherson <seanjc@google.com>
39. **[06-11 15:45]** [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across IRTE
 updates in IOMMU
   - 发件人: Sean Christopherson <seanjc@google.com>
40. **[06-11 15:45]** [PATCH v3 39/62] iommu/amd: Document which IRTE fields
 amd_iommu_update_ga() can modify
   - 发件人: Sean Christopherson <seanjc@google.com>
41. **[06-11 15:45]** [PATCH v3 40/62] iommu/amd: KVM: SVM: Infer IsRun from validity of
 pCPU destination
   - 发件人: Sean Christopherson <seanjc@google.com>
42. **[06-11 15:45]** [PATCH v3 41/62] iommu/amd: Factor out helper for manipulating IRTE
 GA/CPU info
   - 发件人: Sean Christopherson <seanjc@google.com>
43. **[06-11 15:45]** [PATCH v3 42/62] iommu/amd: KVM: SVM: Set pCPU info in IRTE when
 setting vCPU affinity
   - 发件人: Sean Christopherson <seanjc@google.com>
44. **[06-11 15:45]** [PATCH v3 43/62] iommu/amd: KVM: SVM: Add IRTE metadata to affined
 vCPU's list if AVIC is inhibited
   - 发件人: Sean Christopherson <seanjc@google.com>
45. **[06-11 15:45]** [PATCH v3 44/62] KVM: SVM: Don't check for assigned device(s) when
 updating affinity
   - 发件人: Sean Christopherson <seanjc@google.com>
46. **[06-11 15:45]** [PATCH v3 45/62] KVM: SVM: Don't check for assigned device(s) when
 activating AVIC
   - 发件人: Sean Christopherson <seanjc@google.com>
47. **[06-11 15:45]** [PATCH v3 46/62] KVM: SVM: WARN if (de)activating guest mode in IOMMU fails
   - 发件人: Sean Christopherson <seanjc@google.com>
48. **[06-11 15:45]** [PATCH v3 47/62] KVM: SVM: Process all IRTEs on affinity change even
 if one update fails
   - 发件人: Sean Christopherson <seanjc@google.com>
49. **[06-11 15:45]** [PATCH v3 48/62] KVM: SVM: WARN if updating IRTE GA fields in IOMMU fails
   - 发件人: Sean Christopherson <seanjc@google.com>
50. **[06-11 15:45]** [PATCH v3 49/62] KVM: x86: Drop superfluous "has assigned device"
 check in kvm_pi_update_irte()
   - 发件人: Sean Christopherson <seanjc@google.com>
51. **[06-11 15:45]** [PATCH v3 50/62] KVM: x86: WARN if IRQ bypass isn't supported in kvm_pi_update_irte()
   - 发件人: Sean Christopherson <seanjc@google.com>
52. **[06-11 15:45]** [PATCH v3 51/62] KVM: x86: WARN if IRQ bypass routing is updated
 without in-kernel local APIC
   - 发件人: Sean Christopherson <seanjc@google.com>
53. **[06-11 15:45]** [PATCH v3 52/62] KVM: SVM: WARN if ir_list is non-empty at vCPU free
   - 发件人: Sean Christopherson <seanjc@google.com>
54. **[06-11 15:45]** [PATCH v3 53/62] KVM: x86: Decouple device assignment from IRQ bypass
   - 发件人: Sean Christopherson <seanjc@google.com>
55. **[06-11 15:45]** [PATCH v3 54/62] KVM: VMX: WARN if VT-d Posted IRQs aren't possible
 when starting IRQ bypass
   - 发件人: Sean Christopherson <seanjc@google.com>
56. **[06-11 15:45]** [PATCH v3 55/62] KVM: SVM: Use vcpu_idx, not vcpu_id, for GA log tag/metadata
   - 发件人: Sean Christopherson <seanjc@google.com>
57. **[06-11 15:45]** [PATCH v3 56/62] iommu/amd: WARN if KVM calls GA IRTE helpers without
 virtual APIC support
   - 发件人: Sean Christopherson <seanjc@google.com>
58. **[06-11 15:46]** [PATCH v3 57/62] KVM: SVM: Fold avic_set_pi_irte_mode() into its sole caller
   - 发件人: Sean Christopherson <seanjc@google.com>
59. **[06-11 15:46]** [PATCH v3 58/62] KVM: SVM: Don't check vCPU's blocking status when
 toggling AVIC on/off
   - 发件人: Sean Christopherson <seanjc@google.com>
60. **[06-11 15:46]** [PATCH v3 59/62] KVM: SVM: Consolidate IRTE update when toggling AVIC on/off
   - 发件人: Sean Christopherson <seanjc@google.com>
61. **[06-11 15:46]** [PATCH v3 60/62] iommu/amd: KVM: SVM: Allow KVM to control need for
 GA log interrupts
   - 发件人: Sean Christopherson <seanjc@google.com>
62. **[06-11 15:46]** [PATCH v3 61/62] KVM: SVM: Generate GA log IRQs only if the
 associated vCPUs is blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
63. **[06-11 15:46]** [PATCH v3 62/62] KVM: x86: Rename kvm_set_msi_irq() => kvm_msi_to_lapic_irq()
   - 发件人: Sean Christopherson <seanjc@google.com>
64. **[06-12 12:59]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Marc Zyngier <maz@kernel.org>
65. **[06-12 07:34]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
66. **[06-13 19:45]** Re: [PATCH v3 08/62] KVM: SVM: Drop pointless masking of default
 APIC base when setting V_APIC_BAR
   - 发件人: Naveen N Rao <naveen@kernel.org>
67. **[06-13 20:07]** Re: [PATCH v3 09/62] KVM: SVM: Drop pointless masking of kernel page
 pa's with AVIC HPA masks
   - 发件人: Naveen N Rao <naveen@kernel.org>
68. **[06-13 20:08]** Re: [PATCH v3 10/62] KVM: SVM: Add helper to deduplicate code for
 getting AVIC backing page
   - 发件人: Naveen N Rao <naveen@kernel.org>
69. **[06-13 20:14]** Re: [PATCH v3 11/62] KVM: SVM: Drop vcpu_svm's pointless
 avic_backing_page field
   - 发件人: Naveen N Rao <naveen@kernel.org>
70. **[06-13 12:43]** Re: [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type
 changes as changes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
71. **[06-13 13:47]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
72. **[06-13 13:50]** Re: [PATCH v3 33/62] KVM: Fold kvm_arch_irqfd_route_changed() into
 kvm_arch_update_irqfd_routing()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 2: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 46 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 11 Jun 2025 11:47:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM（内核虚拟机）支持 Arm CCA（保密计算架构）的补丁系列（PATCH v9 00/43）。该系列补丁的核心内容是为 KVM 引入对受保护虚拟机的支持，允许在 Arm CCA 环境下运行。

**原始补丁/问题内容**：
补丁系列的目标是实现 KVM 对 Arm CCA 的支持，允许在受保护的虚拟机中运行。补丁中涉及的主要功能包括支持 RMM（Realm Management Monitor）和对 Realm 的管理。

**之前讨论要点**：
历史讨论中提到，相关的来宾支持已在 v6.14-rc1 中合并，因此不再需要单独处理。补丁中还包含了对代码的多项改进和重构，以提高可读性和性能。

**本周新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，包括：
1. 增加了对 RMM 的支持，允许 VMM（虚拟机监控器）配置和管理 Realm。
2. 引入了新的 ioctl 接口以支持 Realm 的创建、配置和激活。
3. 讨论了如何处理 Realm 中的 MMIO（内存映射输入输出）操作，以及如何在 Realm 中管理计时器和 PMU（性能监控单元）。
4. 确保 Realm 的内存管理和地址空间状态（RIPAS）可以动态更新。
5. 讨论了如何处理用户空间对寄存器的访问限制，以及如何在 Realm 中处理 PSCI（电源状态协调接口）请求。

此外，补丁还对用户空间的接口进行了更新，以反映新的功能和能力，包括对私有内存的支持和对 SVE（可扩展向量扩展）的检查。整体来看，补丁系列的目标是增强 KVM 在 Arm CCA 环境下的功能和灵活性。

#### 📝 邮件列表

1. **[06-11 11:47]** [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[06-11 11:47]** [PATCH v9 01/43] kvm: arm64: Include kvm_emulate.h in kvm/arm_psci.h
   - 发件人: Steven Price <steven.price@arm.com>
3. **[06-11 11:47]** [PATCH v9 02/43] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
4. **[06-11 11:48]** [PATCH v9 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
5. **[06-11 11:48]** [PATCH v9 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
6. **[06-11 11:48]** [PATCH v9 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
7. **[06-11 11:48]** [PATCH v9 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
8. **[06-11 11:48]** [PATCH v9 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
9. **[06-11 11:48]** [PATCH v9 08/43] kvm: arm64: Don't expose debug capabilities for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
10. **[06-11 11:48]** [PATCH v9 09/43] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Steven Price <steven.price@arm.com>
11. **[06-11 11:48]** [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
12. **[06-11 11:48]** [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
13. **[06-11 11:48]** [PATCH v9 12/43] KVM: arm64: vgic: Provide helper for number of list registers
   - 发件人: Steven Price <steven.price@arm.com>
14. **[06-11 11:48]** [PATCH v9 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
15. **[06-11 11:48]** [PATCH v9 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
16. **[06-11 11:48]** [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
17. **[06-11 11:48]** [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
18. **[06-11 11:48]** [PATCH v9 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
19. **[06-11 11:48]** [PATCH v9 18/43] KVM: arm64: Handle realm MMIO emulation
   - 发件人: Steven Price <steven.price@arm.com>
20. **[06-11 11:48]** [PATCH v9 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Steven Price <steven.price@arm.com>
21. **[06-11 11:48]** [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
22. **[06-11 11:48]** [PATCH v9 21/43] KVM: arm64: Handle realm VCPU load
   - 发件人: Steven Price <steven.price@arm.com>
23. **[06-11 11:48]** [PATCH v9 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
24. **[06-11 11:48]** [PATCH v9 23/43] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Steven Price <steven.price@arm.com>
25. **[06-11 11:48]** [PATCH v9 24/43] KVM: arm64: WARN on injected undef exceptions
   - 发件人: Steven Price <steven.price@arm.com>
26. **[06-11 11:48]** [PATCH v9 25/43] arm64: Don't expose stolen time for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
27. **[06-11 11:48]** [PATCH v9 26/43] arm64: RME: allow userspace to inject aborts
   - 发件人: Steven Price <steven.price@arm.com>
28. **[06-11 11:48]** [PATCH v9 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
29. **[06-11 11:48]** [PATCH v9 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
30. **[06-11 11:48]** [PATCH v9 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
31. **[06-11 11:48]** [PATCH v9 30/43] arm64: RME: Prevent Device mappings for Realms
   - 发件人: Steven Price <steven.price@arm.com>
32. **[06-11 11:48]** [PATCH v9 31/43] arm_pmu: Provide a mechanism for disabling the physical IRQ
   - 发件人: Steven Price <steven.price@arm.com>
33. **[06-11 11:48]** [PATCH v9 32/43] arm64: RME: Enable PMU support with a realm guest
   - 发件人: Steven Price <steven.price@arm.com>
34. **[06-11 11:48]** [PATCH v9 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
35. **[06-11 11:48]** [PATCH v9 34/43] arm64: RME: Propagate number of breakpoints and watchpoints to userspace
   - 发件人: Steven Price <steven.price@arm.com>
36. **[06-11 11:48]** [PATCH v9 35/43] arm64: RME: Set breakpoint parameters through SET_ONE_REG
   - 发件人: Steven Price <steven.price@arm.com>
37. **[06-11 11:48]** [PATCH v9 36/43] arm64: RME: Initialize PMCR.N with number counter supported by RMM
   - 发件人: Steven Price <steven.price@arm.com>
38. **[06-11 11:48]** [PATCH v9 37/43] arm64: RME: Propagate max SVE vector length from RMM
   - 发件人: Steven Price <steven.price@arm.com>
39. **[06-11 11:48]** [PATCH v9 38/43] arm64: RME: Configure max SVE vector length for a Realm
   - 发件人: Steven Price <steven.price@arm.com>
40. **[06-11 11:48]** [PATCH v9 39/43] arm64: RME: Provide register list for unfinalized RME RECs
   - 发件人: Steven Price <steven.price@arm.com>
41. **[06-11 11:48]** [PATCH v9 40/43] arm64: RME: Provide accurate register list
   - 发件人: Steven Price <steven.price@arm.com>
42. **[06-11 11:48]** [PATCH v9 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>
43. **[06-11 11:48]** [PATCH v9 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user space
   - 发件人: Steven Price <steven.price@arm.com>
44. **[06-11 11:48]** [PATCH v9 43/43] KVM: arm64: Allow activating realms
   - 发件人: Steven Price <steven.price@arm.com>
45. **[06-12 16:14]** Re: [PATCH v9 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Joey Gouly <joey.gouly@arm.com>
46. **[06-12 16:32]** Re: [PATCH v9 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 3: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 30 | **👥 参与者**: 6 | **📅 开始时间**: Wed, 11 Jun 2025 14:33:12 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于KVM（Kernel-based Virtual Machine）中支持guest_memfd（来宾内存文件描述符）备份的内存映射功能，特别是针对软件保护虚拟机的实现。

1. **原始Patch/问题的内容**：
   本次讨论的补丁系列（PATCH v12 00/18）旨在实现主机对guest_memfd备份内存的映射，支持如Firecracker等虚拟机监控程序。这一功能有助于增强对Spectre类攻击的防护，并为机密计算平台提供共享内存的基础。

2. **之前的讨论要点**：
   在之前的版本中，开发者们讨论了如何将“私有”内存的概念与guest_memfd的支持解耦，并对相关配置选项进行了重命名，以提高代码的可读性和维护性。此外，补丁系列还包括对x86和arm64架构的支持。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在多个补丁的审查和反馈上，包括对共享内存支持的实现、内存页故障处理的改进，以及对KVM能力的引入（KVM_CAP_GMEM_SHARED_MEM）。参与者们对补丁的命名和功能进行了细致的讨论，提出了对术语“共享”的不同看法，并建议在代码中使用更明确的命名。此外，多个补丁已获得审核通过，标志着该功能的进一步推进。整体来看，开发者们对补丁的进展表示认可，但也提出了需要进一步优化的地方。

#### 📝 邮件列表

1. **[06-11 14:33]** [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-11 14:33]** [PATCH v12 01/18] KVM: Rename CONFIG_KVM_PRIVATE_MEM to CONFIG_KVM_GMEM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-11 14:33]** [PATCH v12 02/18] KVM: Rename CONFIG_KVM_GENERIC_PRIVATE_MEM to CONFIG_KVM_GENERIC_GMEM_POPULATE
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-11 14:33]** [PATCH v12 03/18] KVM: Rename kvm_arch_has_private_mem() to kvm_arch_supports_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[06-11 14:33]** [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[06-11 14:33]** [PATCH v12 05/18] KVM: Rename kvm_slot_can_be_private() to kvm_slot_has_gmem()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[06-11 14:33]** [PATCH v12 06/18] KVM: Fix comments that refer to slots_lock
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[06-11 14:33]** [PATCH v12 07/18] KVM: Fix comment that refers to kvm uapi header path
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[06-11 14:33]** [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[06-11 14:33]** [PATCH v12 09/18] KVM: guest_memfd: Track shared memory support in memslot
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[06-11 14:33]** [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[06-11 14:33]** [PATCH v12 11/18] KVM: x86: Consult guest_memfd when computing max_mapping_level
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[06-11 14:33]** [PATCH v12 12/18] KVM: x86: Enable guest_memfd shared memory for
 non-CoCo VMs
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[06-11 14:33]** [PATCH v12 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[06-11 14:33]** [PATCH v12 14/18] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[06-11 14:33]** [PATCH v12 15/18] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
17. **[06-11 14:33]** [PATCH v12 16/18] KVM: Introduce the KVM capability KVM_CAP_GMEM_SHARED_MEM
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[06-11 14:33]** [PATCH v12 17/18] KVM: selftests: Don't use hardcoded page sizes in
 guest_memfd test
   - 发件人: Fuad Tabba <tabba@google.com>
19. **[06-11 14:33]** [PATCH v12 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[06-12 21:46]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Shivank Garg <shivankg@amd.com>
21. **[06-12 21:53]** Re: [PATCH v12 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Shivank Garg <shivankg@amd.com>
22. **[06-12 21:54]** Re: [PATCH v12 17/18] KVM: selftests: Don't use hardcoded page sizes
 in guest_memfd test
   - 发件人: Shivank Garg <shivankg@amd.com>
23. **[06-12 10:33]** Re: [PATCH v12 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: James Houghton <jthoughton@google.com>
24. **[06-12 19:38]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
25. **[06-13 06:57]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Ackerley Tng <ackerleytng@google.com>
26. **[06-13 13:35]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[06-13 14:03]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-13 23:18]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
29. **[06-13 15:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
30. **[06-13 15:48]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 4: [PATCH v11 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 18 | **👥 参与者**: 5 | **📅 开始时间**: Thu,  5 Jun 2025 16:37:42 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 的补丁系列，主要内容是实现主机对基于 guest_memfd 的内存的映射，以支持软件保护的虚拟机。补丁的关键改动包括：增加了对共享页面的边界检查、重构了 KVM/arm64 的故障处理逻辑，并处理了嵌套虚拟化的相关问题。

在历史讨论中，Fuad Tabba 提出了多个补丁（共18个），其中包括允许主机映射 guest_memfd 页面、处理基于 guest_memfd 的页面故障等。补丁的设计考虑了共享内存的支持，并通过 KVM_GMEM_SHARED_MEM 配置选项进行控制。

本周的新讨论中，参与者们对补丁进行了审查和反馈。Gavin Shan 对多个补丁表示认可，并提出了一些细节上的建议，例如在处理权限故障时的内存缓存初始化问题。同时，讨论中还涉及了对代码简洁性的建议，强调了使用明确变量名的必要性。整体来看，本周的讨论主要集中在补丁的细节审查和代码优化上，未见重大争议，进展顺利。

#### 📝 邮件列表

1. **[06-05 16:37]** [PATCH v11 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-05 16:37]** [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-05 16:37]** [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-05 16:37]** [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest page faults
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[06-05 16:37]** [PATCH v11 15/18] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[06-05 16:38]** [PATCH v11 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[06-06 11:12]** Re: [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
8. **[06-09 09:43]** Re: [PATCH v11 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[06-09 10:27]** Re: [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Gavin Shan <gshan@redhat.com>
10. **[06-09 10:29]** Re: [PATCH v11 15/18] KVM: arm64: Enable host mapping of shared
 guest_memfd memory
   - 发件人: Gavin Shan <gshan@redhat.com>
11. **[06-09 14:08]** Re: [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Gavin Shan <gshan@redhat.com>
12. **[06-09 08:01]** Re: [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[06-09 08:04]** Re: [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[06-09 08:06]** Re: [PATCH v11 18/18] KVM: selftests: guest_memfd mmap() test when
 mapping is allowed
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[06-09 19:02]** Re: [PATCH v11 13/18] KVM: arm64: Refactor user_mem_abort()
   - 发件人: Gavin Shan <gshan@redhat.com>
16. **[06-09 19:06]** Re: [PATCH v11 14/18] KVM: arm64: Handle guest_memfd-backed guest
 page faults
   - 发件人: Gavin Shan <gshan@redhat.com>
17. **[06-11 11:59]** Re: [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Shivank Garg <shivankg@amd.com>
18. **[06-11 11:20]** Re: [PATCH v11 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 5: [PATCH v7 00/14] arm: rework id register storage

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 06 Jun 2025 11:53:15 +0200

#### 🤖 AI 总结

本邮件线程讨论的主题是对 ARM 架构中 ID 寄存器存储的重新设计，具体内容为一个包含 14 个补丁的系列（PATCH v7 00/14）。历史讨论中，Cornelia Huck 提到该补丁系列的总体思路是可行的，但指出了一些编译失败和需要重基的地方。

在本周的新讨论中，Peter Maydell 针对多个补丁（如补丁 2、8、12 和 13）提出了编译错误的反馈，指出了指针类型不兼容的问题，并讨论了生成脚本的命名和使用语言（建议使用 Python 而非 awk）。Cornelia Huck 也提到了一些寄存器的使用问题，认为某些寄存器并不简单，可能不适合包含在 ID 寄存器数组中。

此外，参与者们讨论了编译环境和配置，Peter 表示会在每个补丁后进行自动化构建，以避免遗漏编译问题。整体来看，本周的讨论集中在补丁的编译问题、生成脚本的改进以及寄存器的适用性上，显示出对代码质量和可维护性的关注。

#### 📝 邮件列表

1. **[06-06 11:53]** Re: [PATCH v7 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-12 16:04]** Re: [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
3. **[06-12 16:16]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
4. **[06-12 16:29]** Re: [PATCH v7 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
5. **[06-12 17:34]** Re: [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[06-12 16:35]** Re: [PATCH v7 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
7. **[06-12 17:36]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[06-12 16:36]** Re: [PATCH v7 00/14] arm: rework id register storage
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
9. **[06-12 16:39]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
10. **[06-12 16:39]** Re: [PATCH v7 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the
 idregs arrays
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
11. **[06-12 17:42]** Re: [PATCH v7 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[06-12 17:53]** Re: [PATCH v7 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[06-12 18:07]** Re: [PATCH v7 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 6: [PATCH 0/8] KVM: Remove include/kvm, standardize includes

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 10 Jun 2025 17:10:34 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于KVM（Kernel-based Virtual Machine）的一系列补丁，主要目标是移除`include/kvm`目录并标准化各架构的包含路径。

**原始补丁内容**：
补丁的核心是通过移动和重命名文件，删除`include/kvm`目录，并在所有架构中统一KVM的包含路径。这一变更为后续的分区PMU（Performance Monitoring Unit）工作做了准备。

**之前讨论要点**：
在之前的讨论中，Sean Christopherson提到这些补丁是一个较大RFC（请求反馈）的一部分，虽然多KVM的想法已被放弃，但他希望能逐步上游那些有益的部分。补丁也与Colton的分区PMU系列存在冲突。

**本周新讨论和进展**：
本周的讨论中，Sean Christopherson提交了多个补丁，涵盖了不同架构（如ARM、MIPS、PPC、s390等）的文件移动和包含路径的标准化。讨论中提到，MIPS和PPC等架构不再将`virt/kvm`添加到包含路径中，因为这些头文件仅供KVM核心代码使用。此外，Paolo Bonzini和Oliver Upton等人对补丁表示认可，并计划尽快将其合并到KVM的下一个版本中。整体来看，补丁的推进得到了积极的反馈，预计将很快实现。

#### 📝 邮件列表

1. **[06-10 17:10]** [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-10 17:10]** [PATCH 1/8] KVM: arm64: Move arm_{psci,hypercalls}.h to an internal
 KVM path
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-10 17:10]** [PATCH 2/8] KVM: arm64: Include KVM headers to get forward declarations
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-10 17:10]** [PATCH 3/8] KVM: arm64: Move ARM specific headers in include/kvm to
 arch directory
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-10 17:10]** [PATCH 4/8] KVM: Move include/kvm/iodev.h to include/linux as kvm_iodev.h
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-10 17:10]** [PATCH 5/8] KVM: MIPS: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-10 17:10]** [PATCH 6/8] KVM: PPC: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-10 17:10]** [PATCH 7/8] KVM: s390: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[06-10 17:10]** [PATCH 8/8] KVM: Standardize include paths across all architectures
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-12 06:56]** Re: [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
11. **[06-12 15:01]** Re: [PATCH 7/8] KVM: s390: Stop adding virt/kvm to the arch include
 path
   - 发件人: Janosch Frank <frankja@linux.ibm.com>
12. **[06-13 14:02]** Re: [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases fixes

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Thu,  5 Jun 2025 12:36:09 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测修复补丁，主要集中在 `arch_timer_edge_cases` 的修复上。

1. **原始补丁内容**：Sebastian Ott 提交的补丁（[PATCH v3 0/4]）包含四个小修复，旨在解决在 ampere-one 上运行自测时遇到的失败问题。补丁中提到根据 Marc 的建议确定有效计数器宽度，并新增了修复 `xval` 初始化的补丁。

2. **之前讨论要点**：在历史讨论中，Sebastian 提到他在多台机器上进行了测试，未发现问题。Miguel Luis 反馈了在不同条件下的测试结果，指出在某些情况下测试未能返回。

3. **本周新讨论与进展**：本周的讨论主要围绕补丁的测试与验证。Miguel 继续尝试重现未返回的情况，Sebastian 表示会设置环境进行测试。此外，Raghavendra Rao Ananta 提出了与 GIC（Generic Interrupt Controller）相关的新补丁，旨在引入控制 GICD_TYPER2.nASSGIcap 属性的功能，以便用户空间能够按需控制 VM 的中断支持。该系列补丁还包括对 VGIC 的自测，确保在 VGIC 初始化前可以配置相关属性。Oliver Upton 提醒 Raghavendra 在提交补丁时需注意检查格式问题。

总的来说，本周的讨论集中在补丁的测试结果和进一步的功能扩展上，参与者们积极交流以确保补丁的有效性和稳定性。

#### 📝 邮件列表

1. **[06-05 12:36]** [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases fixes
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[06-09 17:26]** Re: [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases fixes
   - 发件人: Miguel Luis <miguel.luis@oracle.com>
3. **[06-10 15:50]** Re: [PATCH v3 0/4] KVM: arm64: selftests: arch_timer_edge_cases
 fixes
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[06-13 15:52]** [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
5. **[06-13 15:52]** [PATCH v3 1/4] KVM: arm64: Disambiguate support for vSGIs v. vLPIs
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
6. **[06-13 15:52]** [PATCH v3 2/4] KVM: arm64: vgic-v3: Consolidate MAINT_IRQ handling
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
7. **[06-13 15:52]** [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
8. **[06-13 15:52]** [PATCH v3 4/4] KVM: arm64: selftests: Add test for nASSGIcap attribute
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
9. **[06-13 13:53]** Re: [PATCH v3 0/4] KVM: arm64: Add attribute to control
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-13 14:25]** Re: [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>

---

### Thread 8: [PATCH v23 0/4] arm64/perf: Enable branch stack sampling

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 11 Jun 2025 13:01:10 -0500

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的分支记录缓冲扩展（BRBE）的支持，主要通过一系列补丁实现。补丁的核心内容是启用 BRBE 功能，以便在执行过程中记录分支信息，类似于 x86 的最后分支记录（LBR）。

历史讨论方面，补丁系列从 Anshuman Khandual 开始，Rob Herring 进行了后续的重构和更新。补丁版本 v23 主要包括对 BRBE 的支持、相关寄存器的定义、引导要求的处理以及在 KVM 虚拟化环境中对分支生成的管理。

本周的新讨论中，Rob Herring 提供了补丁的详细更新，包括对 BRBE 的初始化、在 nVHE 模式下的特殊处理，以及在 KVM 中如何禁用来宾的分支记录。Adam Young 反馈了在 BRBE 支持的机器上进行的测试，确认了该功能的有效性，并且能够成功生成和处理 perf.data 文件，进一步验证了补丁的可靠性。

总结来说，本周的讨论集中在补丁的实施细节和测试结果上，显示出 BRBE 功能在 ARM64 架构中的实际应用潜力。

#### 📝 邮件列表

1. **[06-11 13:01]** [PATCH v23 0/4] arm64/perf: Enable branch stack sampling
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
2. **[06-11 13:01]** [PATCH v23 1/4] arm64/sysreg: Add BRBE registers and fields
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
3. **[06-11 13:01]** [PATCH v23 2/4] arm64: Handle BRBE booting requirements
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
4. **[06-11 13:01]** [PATCH v23 3/4] KVM: arm64: nvhe: Disable branch generation in
 nVHE guests
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
5. **[06-11 13:01]** [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch Record
 Buffer Extension (BRBE)
   - 发件人: Rob Herring (Arm) <robh@kernel.org>
6. **[06-12 13:13]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Adam Young <admiyo@amperemail.onmicrosoft.com>
7. **[06-12 15:28]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Rob Herring <robh@kernel.org>
8. **[06-12 23:16]** Re: [PATCH v23 2/4] arm64: Handle BRBE booting requirements
   - 发件人: Adam Young <admiyo@amperemail.onmicrosoft.com>
9. **[06-12 23:19]** Re: [PATCH v23 4/4] perf: arm_pmuv3: Add support for the Branch
 Record Buffer Extension (BRBE)
   - 发件人: Adam Young <admiyo@amperemail.onmicrosoft.com>

---

### Thread 9: [PATCH v4 0/5] Add FIELD_MODIFY() helper

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 12 Jun 2025 21:46:07 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于添加 `FIELD_MODIFY()` 辅助宏的补丁系列（PATCH v4 0/5）。该宏旨在增强现有的 `FIELD_XXX` 宏家族，提供编译时类型检查，以避免参数类型错误。补丁还包括将内核核心文件中四个使用原始编码的 `FIELD_MODIFY()` 实例转换为新宏的实现，转换过程使用了 Coccinelle 工具。

在历史讨论中，补丁的版本经历了多次修改，主要集中在改进文档示例、修复 Coccinelle 脚本中的问题以及对补丁的描述进行优化。每个版本都链接到之前的版本以便于追踪。

在本周的新讨论中，Luo Jie 提交了五个具体的补丁，分别针对 ARM64 架构的不同文件进行 `FIELD_MODIFY()` 的应用。尽管补丁的实现得到了详细说明，但参与者 Marc Zyngier 表达了对该补丁的反对意见，认为现有的辅助函数已经足够，并不需要重复实现相同功能。另一位参与者 Markus Elfring 提出了对补丁描述的进一步优化建议，强调了补丁版本描述的重要性以及简化条件选择的可能性。

总体来看，尽管补丁的实现和讨论进展顺利，但仍然面临一些反对意见和改进建议。

#### 📝 邮件列表

1. **[06-12 21:46]** [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-12 21:46]** [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
3. **[06-12 21:46]** [PATCH v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
4. **[06-12 21:46]** [PATCH v4 3/5] arm64: nvhe: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
5. **[06-12 21:46]** [PATCH v4 4/5] arm64: kvm: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
6. **[06-12 21:46]** [PATCH v4 5/5] arm64: mm: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
7. **[06-12 15:11]** Re: [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[06-12 18:48]** Re: [cocci] [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
9. **[06-12 22:15]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Markus Elfring <Markus.Elfring@web.de>

---

### Thread 10: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Mon, 26 May 2025 21:26:52 -0300

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构中引入的新内存槽标志的补丁，该标志用于指示可缓存的映射。补丁的目的是为了改善虚拟机监控器（VMM）在处理内存属性时的灵活性。

在历史讨论中，参与者对该补丁的必要性和实现方式进行了激烈的辩论。Jason Gunthorpe 表示反对，认为该补丁增加了创建内存槽的复杂性，且 VFIO（虚拟功能 I/O）无法轻易识别何时设置该标志。Ankit Agrawal 和 Oliver Upton 提出了不同的观点，认为引入标志可以帮助 VMM 更好地表达其意图，但 Sean Christopherson 认为该补丁不应包含在 KVM 的用户 API 中，认为其实现混乱。

在本周的新讨论中，Jason Gunthorpe 和 Sean Christopherson 进一步探讨了 PFNMAP（页面框架号映射）与缓存管理操作（CMO）之间的关系，强调了代码的清晰性和逻辑性。Oliver Upton 也表示，虽然没有完整的解决方案，但在缺乏细粒度枚举的情况下，可以暂时放弃该内存槽标志，认为 KVM 的能力仍然是有用的。

总体来看，尽管对补丁的讨论仍在继续，但参与者们对如何处理内存属性和映射的理解逐渐趋于一致，未来可能会在 KVM 6.17 版本中达成某种共识。

#### 📝 邮件列表

1. **[05-26 21:26]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
2. **[05-27 04:33]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable
 mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
3. **[06-06 10:57]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-06 11:11]** Re: [PATCH v6 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-09 09:24]** Re: [PATCH v6 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
6. **[06-09 07:21]** Re: [PATCH v6 1/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-13 12:38]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 11: [PATCH V4 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 12 Jun 2025 09:05:45 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下的调试宏的优化，主要集中在删除冗余的 `DBG_MDSCR_*` 宏。原始的补丁（PATCH V4 0/2）提出了这一优化，理由是 `MDSCR_EL1` 已在工具的 sysreg 格式中定义，因此可以直接使用，相关的 `DBG_MDSCR_*` 宏显得多余。

在历史讨论中，补丁经历了多个版本的修改，主要是为了更新提交信息、调整变量类型为 `u64` 以反映其真实宽度，并将自测代码的更改分离到单独的补丁中。参与者们对补丁的内容进行了审查和反馈，确保代码的准确性和一致性。

本周的新讨论中，Anshuman Khandual 提出了补丁的最新版本，进一步修改了变量类型并解决了编译警告。Marc Zyngier 提出了建议，要求在其他地方也使用 `MDSCR_EL1_TDCC` 常量替代硬编码的值。Anshuman 表示会将该建议纳入补丁中，并讨论了使用 `mov` 指令的优先性。

总体而言，本周的讨论集中在补丁的细节调整和代码优化上，参与者们积极交流，推动了补丁的完善。

#### 📝 邮件列表

1. **[06-12 09:05]** [PATCH V4 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[06-12 09:05]** [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[06-12 09:05]** [PATCH V4 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[06-12 09:17]** Re: [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[06-12 15:54]** Re: [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[06-12 11:51]** Re: [PATCH V4 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v3 00/10] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 05 Jun 2025 11:48:58 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.8 SPE 特性的补丁（PATCH v3 00/10），主要涉及三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 FEAT_SPE_FDS 数据源过滤。这些特性相互独立，可以单独应用。补丁的前两部分涉及系统寄存器的变更，后续补丁则针对不同特性进行支持。

在历史讨论中，James Clark 提出了补丁的具体内容，并介绍了每个特性的实现细节。邮件中提到，FEAT_SPEv1p4 需要对之前版本的 RES0 位进行调整，同时 FEAT_SPE_EFT 和 FEAT_SPE_FDS 也需要相应的系统寄存器支持。

本周的新讨论中，Anshuman Khandual 对补丁的部分内容进行了审查，确认了新寄存器字段与 ARM 文档的一致性，并提出了对 PMSEVFR_EL1_RES0_V1P4 过滤器的实现方式的疑问。他建议是否可以直接添加所有新过滤位，而不是使用排除和包含的方式。James Clark 回应了这一点，解释了这样做的原因是为了避免重复定义，并保持一致性。

总体来看，本周的讨论主要集中在对补丁实现细节的审查和优化建议上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[06-05 11:48]** [PATCH v3 00/10] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[06-05 11:48]** [PATCH v3 01/10] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: James Clark <james.clark@linaro.org>
3. **[06-05 11:49]** [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>
4. **[06-12 12:14]** Re: [PATCH v3 01/10] arm64: sysreg: Add new PMSFCR_EL1 fields and
 PMSDSFR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[06-12 13:05]** Re: [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[06-12 09:42]** Re: [PATCH v3 02/10] perf: arm_spe: Support FEAT_SPEv1p4 filters
   - 发件人: James Clark <james.clark@linaro.org>

---

### Thread 13: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 10 Jun 2025 11:01:28 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测中的一个补丁（PATCH V3 2/2），其主要内容是将 MDSCR_EL1 寄存器的局部变量类型更改为 uint64_t，以反映其真实的寄存器宽度。这一补丁由 Anshuman Khandual 提出，并得到了 Ada Couprie Diaz 的审核。

在历史讨论中，参与者们关注到 MDSCR_EL1 寄存器在代码中的使用，Marc Zyngier 指出，虽然在自测代码中进行了更改，但在其他文件（如 arch/arm64/kernel/debug-monitors.c）中仍然存在大量的 32 位操作，建议对相关代码进行全面更新，而不是仅在一个随机文件中进行局部更改。

本周的新讨论中，Marc Zyngier 对补丁提出了质疑，认为应在更重要的地方进行更改，并强调了补丁系列的上下文需要更清晰。Mark Rutland 也指出，Anshuman 在补丁的发送中未能将 Marc Cc 上，导致信息传递不够完整。Anshuman 随后承诺会更好地描述补丁的理由，并确保相关人员在后续讨论中得到通知。

总体来看，本周讨论集中在补丁的合理性和上下文的重要性上，参与者们希望能更全面地解决 MDSCR_EL1 寄存器的处理问题。

#### 📝 邮件列表

1. **[06-10 11:01]** [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[06-10 18:01]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-11 09:15]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding
 variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[06-11 10:59]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding
 variables as uint64_t
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[06-11 13:52]** Re: [PATCH V3 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc

**📧 邮件数**: 4 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 10 Jun 2025 20:41:32 +0530

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个构建失败问题的修复补丁。补丁的主要内容是解决在使用 aarch64-linux-gnu-gcc 版本 13.3.0 时出现的构建错误，具体表现为未定义符号 `__kvm_nvhe___lshrti3` 的引用问题。为了解决这个问题，补丁中引入了一个新的辅助函数，类似于之前的提交（9bfe7553fadb）中实现的 `__lshrti3` 函数。

在之前的讨论中，参与者们关注了导致构建失败的原因，并探讨了相关的代码变更。Aneesh Kumar 提到，这个问题与最近引入的 pKVM tracefs 补丁有关。

本周的新讨论中，Aneesh Kumar 进一步确认了补丁的背景，并提到与 pKVM 追踪支持相关的代码尚未合并到主线。Marc Zyngier 则询问了触发此问题的具体原因，并希望了解如何避免类似问题的发生。Vincent Donnefort 也补充说明了相关文件尚未上游的问题。整体来看，讨论围绕着补丁的必要性及其背景展开，参与者们对如何解决构建失败问题表现出积极的关注。

#### 📝 邮件列表

1. **[06-10 20:41]** [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Aneesh Kumar K.V (Arm) <aneesh.kumar@kernel.org>
2. **[06-10 20:47]** Re: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
3. **[06-10 16:31]** Re: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-10 16:48]** Re: [PATCH] KVM: arm64: nvhe: Fix build failure with gcc
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 15: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 28 May 2025 10:30:20 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下添加对 KVM_MEM_USERFAULT 的支持的补丁（PATCH v2 06/13）。在历史讨论中，参与者 Sean Christopherson 和 James Houghton 进行了深入的技术探讨，主要围绕补丁中的代码片段及其潜在问题展开。Sean 指出补丁存在一些错误，并提供了具体的代码差异（diff）以便于修正。两人讨论了与旧标志和新标志相关的逻辑问题，尤其是在启用脏日志记录时的行为。

在本周的新讨论中，James Houghton 对之前的混淆表示歉意，承认自己将 KVM_MEM_USERFAULT 和 KVM_MEM_LOG_DIRTY_PAGES 混淆了。他决定撤回之前提到的修改，并感谢 Sean 的指正。这表明参与者之间的沟通有效，能够及时纠正错误并推动补丁的完善。整体来看，讨论进展顺利，补丁的修正方向已经明确。

#### 📝 邮件列表

1. **[05-28 10:30]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[05-28 20:17]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: James Houghton <jthoughton@google.com>
3. **[05-28 16:25]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-09 16:04]** Re: [PATCH v2 06/13] KVM: arm64: Add support for KVM_MEM_USERFAULT
   - 发件人: James Houghton <jthoughton@google.com>

---

### Thread 16: [PATCH V5 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 13 Jun 2025 08:06:44 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM64 架构下的调试宏的优化，主要集中在删除冗余的 `DBG_MDSCR_*` 宏。原始的补丁（PATCH V5 0/2）提出了这一点，指出 `MDSCR_EL1` 已在工具的系统寄存器格式中定义，因此可以在所有调试监控相关的调用路径中使用，进而使得所有 `DBG_MDSCR_*` 宏变得冗余。

在之前的讨论中，补丁经历了多个版本的修改，主要集中在变量类型的更改上，例如将处理 `MDSCR_EL1` 寄存器的变量类型改为 `u64`，以反映其真实宽度。此外，补丁还解决了使用生成的系统寄存器定义时出现的构建警告。

在本周的新讨论中，Anshuman Khandual 提出了补丁的最新版本，进一步明确了在 `__cpu_setup()` 中替换开放编码为 `MDSCR_EL1_TDCC` 的必要性，并对相关代码进行了相应的修改。补丁得到了 Ada Couprie Diaz 的审核通过，显示出该修改的认可和支持。此外，针对 KVM 自测的补丁（PATCH V5 2/2）也进行了更新，将 `MDSCR_EL1` 寄存器相关的局部变量改为 `uint64_t`，以确保一致性和准确性。整体来看，本周的讨论推动了补丁的进一步完善和实施。

#### 📝 邮件列表

1. **[06-13 08:06]** [PATCH V5 0/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[06-13 08:06]** [PATCH V5 1/2] arm64/debug: Drop redundant DBG_MDSCR_* macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[06-13 08:06]** [PATCH V5 2/2] KVM: selftests: Change MDSCR_EL1 register holding variables as uint64_t
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 17: [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Sun, 8 Jun 2025 17:54:02 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试补丁，旨在关闭 GIC（通用中断控制器）文件描述符，以便正确清理虚拟机并消除运行 `arch_timer_edge_cases` 时出现的重复目录警告。

在历史讨论中，Zenghui Yu 提出了这个补丁，主要修改了 `arch_timer_edge_cases.c` 文件，增加了对 GIC FD 的关闭操作，以释放其对虚拟机的引用。补丁的目的是提高虚拟机的清理效率，并解决相关的调试警告。

在本周的新讨论中，参与者 Sebastian Ott 和 Miguel Luis 对该补丁进行了审核，并分别给予了“Reviewed-by”标记，表示他们支持该补丁的合并。这表明补丁得到了积极的反馈，可能会在后续版本中被采纳。整体来看，讨论进展顺利，补丁得到了认可，预计将推动 KVM 的进一步优化。

#### 📝 邮件列表

1. **[06-08 17:54]** [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[06-10 14:38]** Re: [PATCH] KVM: arm64: selftests: Close the GIC FD in
 arch_timer_edge_cases
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[06-11 09:47]** Re: [PATCH] KVM: arm64: selftests: Close the GIC FD in
 arch_timer_edge_cases
   - 发件人: Miguel Luis <miguel.luis@oracle.com>

---

### Thread 18: [PATCH v2 00/15] Add KVM Selftests runner

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Jun 2025 16:56:04 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM 自测试运行器的补丁（PATCH v2 00/15），由 Vipin Sharma 提出。该补丁的主要目的是创建一个 KVM 自测试运行器，以便在自测试框架中运行 KVM 自测试时，提供比默认运行器更多的功能。这些功能包括输出保留、输出详细程度控制、并行执行以及不同命令行参数组合的支持，旨在简化贡献者和维护者的测试过程。

在历史讨论中，Vipin Sharma 详细介绍了该补丁的两个主要目标：一是简化测试配置的运行，二是提供一个统一的平台用于编写有趣且有用的测试组合。此外，补丁的最后一部分还增加了针对 RISC-V 平台的自动生成测试文件。

本周的新讨论中，Andrew Jones 对 Vipin Sharma 的补丁进行了简单的回复，确认了补丁中提到的 RISC-V 相关内容。这表明该补丁在社区中得到了关注，且参与者对补丁的内容表示认可。整体来看，讨论围绕 KVM 自测试运行器的功能扩展及其对开发者的便利性展开，显示出社区对改进测试工具的积极态度。

#### 📝 邮件列表

1. **[06-06 16:56]** [PATCH v2 00/15] Add KVM Selftests runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
2. **[06-06 16:56]** [PATCH v2 15/15] KVM: selftests: Add riscv auto generated test files
 for KVM Selftests Runner
   - 发件人: Vipin Sharma <vipinsh@google.com>
3. **[06-09 14:54]** Re: [PATCH v2 15/15] KVM: selftests: Add riscv auto generated test
 files for KVM Selftests Runner
   - 发件人: Andrew Jones <ajones@ventanamicro.com>

---

### Thread 19: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 14 Jun 2025 22:57:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `vgic_v3_put_nested()` 函数中对 `s_cpu_if->vgic_lr[]` 索引的错误。

补丁的核心内容是，`s_cpu_if->vgic_lr[]` 数组应从索引 0 开始连续填充到 `s_cpu_if->used_lrs - 1`，但在 `vgic_v3_put_nested()` 函数中，该数组的索引却是基于 `shadow_if->lr_map` 中设置位的位置进行的。这种不一致可能导致错误的内存访问，因此补丁通过引入一个新的索引变量 `index` 来修正这一问题。

在之前的讨论中没有提及相关的历史背景或其他补丁，因此本周的新讨论主要集中在 Wei-Lin Chang 提出的这一补丁上。邮件中详细描述了补丁的修改内容，包括对相关代码的具体更改，确保了 `vgic_lr` 数组的正确索引方式。

总的来说，本周的讨论主要是对该补丁的提出和代码实现的详细说明，没有其他参与者的反馈或进一步的讨论。

#### 📝 邮件列表

1. **[06-14 22:57]** [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>

---

### Thread 20: [PATCH v5 0/6] KVM: lockdep improvements

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 10 Jun 2025 16:28:29 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）的锁依赖性（lockdep）改进的补丁系列，标识为 PATCH v5 0/6。该补丁系列的主要内容包括对互斥锁的改进和对 KVM 中虚拟 CPU 锁定机制的优化。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁系列旨在提升 KVM 的锁管理效率，减少潜在的死锁风险，并增强系统的稳定性。

本周的新讨论中，参与者 Paolo Bonzini 确认了该补丁系列已被应用到 riscv/linux.git 的修复分支中，并提供了每个补丁的链接。补丁包括实现新的互斥锁功能（如 `mutex_trylock_nested` 和 `mutex_lock_killable_nest_lock`），以及在 KVM 中添加 `kvm_lock_all_vcpus` 和 `kvm_trylock_all_vcpus` 的实现。这些改进将有助于在不同架构（如 x86 和 arm64）中更有效地管理虚拟 CPU 的锁定。

总的来说，本周的进展表明该补丁系列得到了认可并成功合并，为 KVM 的锁管理提供了重要的改进。

#### 📝 邮件列表

1. **[06-10 16:28]** Re: [PATCH v5 0/6] KVM: lockdep improvements
   - 发件人: patchwork-bot+linux-riscv@kernel.org

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to
 run guest code in vEL2

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 9 Jun 2025 12:14:36 +0900

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to run guest code in vEL2”，主要讨论了在 KVM（Kernel-based Virtual Machine）环境下，针对 arm64 架构的自测试功能的补丁。

在历史讨论部分，由于没有相关内容，因此我们无法提供背景信息。

在本周的新讨论中，参与者 Ganapatrao Kulkarni 提到，该补丁系列（v2）是基于最新的 kvmarm-next 内核，并在 QEMU 的 TCG 模式下进行了测试，特别是添加了 kvm-arm.mode=nested 选项以支持嵌套虚拟化。测试结果由 Itaru Kitayama 确认，表示补丁在其环境中成功运行。

总结而言，本周的讨论集中在补丁的测试情况上，确认了其在特定环境下的有效性，为后续的开发和完善提供了积极的反馈。

#### 📝 邮件列表

1. **[06-09 12:14]** Re: [RFC PATCH v2 2/9] KVM: arm64: nv: selftests: Add simple test to
 run guest code in vEL2
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

## 📌 Bug Report

共 1 个 thread

---

### Thread 1: pkvm boot failures

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 09 Jun 2025 18:53:40 +0530

#### 🤖 AI 总结

本邮件讨论主题为“pkvm启动失败”，主要集中在Linux内核中pKVM（保护虚拟机）功能的启动问题。

1. **原始问题**：参与者Aneesh Kumar K.V报告在使用v6.15内核时遇到启动失败，具体表现为内核恐慌，提示无法转储pKVM nVHE堆栈跟踪。经过排查，发现与配置项`CONFIG_PROTECTED_NVHE_STACKTRACE`有关。

2. **之前讨论要点**：虽然没有历史讨论，但Aneesh提到他找到了一份能够正常工作的内核配置，但未能识别出导致差异的具体配置项。

3. **本周新讨论与进展**：本周的讨论主要围绕`CONFIG_JUMP_LABEL=n`配置项展开。Mostafa Saleh指出，内核在访问`kvm_protected_mode_initialized`变量时出现问题，导致内核恐慌。为解决此问题，Mostafa提出将该变量的定义移至hypervisor命名空间，并引入新的静态键`kvm_protected_mode_initialized_hyp`。Marc Zyngier则建议在KVM配置中强制启用`JUMP_LABEL`，以避免此类问题的重复出现。最终，参与者达成共识，认为需要更新相关函数以支持新的静态键，并在代码中添加注释以防未来的潜在问题。

总体来看，本周的讨论推动了对pKVM启动失败问题的深入分析，并提出了具体的解决方案和改进建议。

#### 📝 邮件列表

1. **[06-09 18:53]** pkvm boot failures
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
2. **[06-09 17:24]** Re: pkvm boot failures
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-09 17:25]** Re: pkvm boot failures
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[06-10 12:03]** Re: pkvm boot failures
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
5. **[06-10 08:34]** Re: pkvm boot failures
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[06-10 09:03]** Re: pkvm boot failures
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[06-10 09:06]** Re: pkvm boot failures
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  6 Jun 2025 10:43:50 +0100

#### 🤖 AI 总结

本邮件线程讨论了 KVM/arm64 在 6.16 版本中的修复补丁。历史讨论中，Marc Zyngier 提交了第二批修复，主要涉及系统寄存器访问器的重大重构，以确保 RES0/RES1 的清理在适当的时机应用。此外，还修复了一个从未正常工作的自测功能。

在本周的新讨论中，Paolo Bonzini 对 Marc 的补丁表示感谢并确认已将其合并。这表明补丁得到了认可并成功集成到代码库中。

总结而言，历史讨论中提出的补丁主要解决了系统寄存器访问和自测功能的问题，而本周的进展则是确认了这些修复已被合并，标志着该问题的解决。

#### 📝 邮件列表

1. **[06-06 10:43]** [GIT PULL] KVM/arm64 fixes for 6.16, take #2
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[06-11 20:25]** Re: [GIT PULL] KVM/arm64 fixes for 6.16, take #2
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

