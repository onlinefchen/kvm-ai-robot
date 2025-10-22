# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:09:18

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 263
- **总 Thread 数**: 31
- **大型 Thread** (>20封): 2 个

### 分类分布

- **PATCH**: 30 threads (259 邮件)
- **RFC**: 1 threads (4 邮件)

---

## 📌 PATCH

共 30 个 thread

---

### Thread 1: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 67 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 16 Apr 2025 14:41:22 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 Arm CCA 支持的补丁系列（PATCH v8 00/43），主要集中在 Arm Confidential Compute Architecture (CCA) 下运行受保护虚拟机的实现。

**原始补丁内容**：
补丁系列旨在为 KVM 添加对 Arm CCA 的支持，允许在虚拟机中运行受保护的计算。补丁包括对新 ioctl 的定义、用户 ABI 的定义，以及创建和配置领域（realm）的功能。

**历史讨论要点**：
在之前的讨论中，补丁经过多次修改，增加了文档说明，调整了结构体和函数的命名，确保了补丁的兼容性和可读性。参与者们对补丁的细节进行了审查和反馈，确保实现的正确性和完整性。

**本周新讨论及进展**：
本周的讨论主要集中在对补丁的细节审查上，参与者提出了一些小的修改建议和命名上的调整。Suzuki K Poulose 和 Gavin Shan 对补丁的各个部分进行了逐一审查，并表示认可。特别是对用户 ABI 的定义和领域创建的流程进行了详细讨论，确保在激活领域后无法再修改内存配置或添加新的 VCPU。此外，讨论中还提到了一些实现中的潜在问题，如 RCU 停滞的报告，表明在实际测试中遇到的挑战。

总体来看，补丁系列在社区的积极讨论和反馈中逐步完善，朝着实现 KVM 对 Arm CCA 支持的目标迈进。

#### 📝 邮件列表

1. **[04-16 14:41]** [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[04-16 14:41]** [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
3. **[04-16 14:41]** [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
4. **[04-16 14:41]** [PATCH v8 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
5. **[04-16 14:41]** [PATCH v8 08/43] kvm: arm64: Don't expose debug capabilities for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
6. **[04-16 14:41]** [PATCH v8 09/43] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Steven Price <steven.price@arm.com>
7. **[04-16 14:41]** [PATCH v8 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
8. **[04-16 14:41]** [PATCH v8 12/43] KVM: arm64: vgic: Provide helper for number of list registers
   - 发件人: Steven Price <steven.price@arm.com>
9. **[04-16 14:41]** [PATCH v8 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
10. **[04-16 14:41]** [PATCH v8 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
11. **[04-16 14:41]** [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
12. **[04-16 14:41]** [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
13. **[04-16 14:41]** [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
14. **[04-16 14:41]** [PATCH v8 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
15. **[04-16 14:41]** [PATCH v8 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
16. **[04-16 14:41]** [PATCH v8 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
17. **[04-16 14:41]** [PATCH v8 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
18. **[04-16 14:41]** [PATCH v8 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
19. **[04-16 14:41]** [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and watchpoints to userspace
   - 发件人: Steven Price <steven.price@arm.com>
20. **[04-16 14:41]** [PATCH v8 36/43] arm64: RME: Initialize PMCR.N with number counter supported by RMM
   - 发件人: Steven Price <steven.price@arm.com>
21. **[04-16 14:41]** [PATCH v8 37/43] arm64: RME: Propagate max SVE vector length from RMM
   - 发件人: Steven Price <steven.price@arm.com>
22. **[04-16 14:42]** [PATCH v8 38/43] arm64: RME: Configure max SVE vector length for a Realm
   - 发件人: Steven Price <steven.price@arm.com>
23. **[04-16 14:42]** [PATCH v8 39/43] arm64: RME: Provide register list for unfinalized RME RECs
   - 发件人: Steven Price <steven.price@arm.com>
24. **[04-16 14:42]** [PATCH v8 40/43] arm64: RME: Provide accurate register list
   - 发件人: Steven Price <steven.price@arm.com>
25. **[04-16 14:42]** [PATCH v8 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>
26. **[04-16 14:42]** [PATCH v8 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user space
   - 发件人: Steven Price <steven.price@arm.com>
27. **[04-16 14:42]** [PATCH v8 43/43] KVM: arm64: Allow activating realms
   - 发件人: Steven Price <steven.price@arm.com>
28. **[04-25 12:08]** Re: [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
29. **[04-28 09:58]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
30. **[04-29 10:45]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
31. **[04-30 14:25]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Gavin Shan <gshan@redhat.com>
32. **[04-30 15:39]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Gavin Shan <gshan@redhat.com>
33. **[04-30 15:42]** Re: [PATCH v8 08/43] kvm: arm64: Don't expose debug capabilities for
 realm guests
   - 发件人: Gavin Shan <gshan@redhat.com>
34. **[04-30 15:47]** Re: [PATCH v8 09/43] KVM: arm64: Allow passing machine type in KVM
 creation
   - 发件人: Gavin Shan <gshan@redhat.com>
35. **[04-30 15:54]** Re: [PATCH v8 12/43] KVM: arm64: vgic: Provide helper for number of
 list registers
   - 发件人: Gavin Shan <gshan@redhat.com>
36. **[04-30 21:38]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
37. **[04-30 21:55]** Re: [PATCH v8 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Gavin Shan <gshan@redhat.com>
38. **[04-30 22:11]** Re: [PATCH v8 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Gavin Shan <gshan@redhat.com>
39. **[05-01 10:16]** Re: [PATCH v8 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
40. **[05-01 12:54]** Re: [PATCH v8 22/43] KVM: arm64: Validate register access for a Realm
 VM
   - 发件人: Gavin Shan <gshan@redhat.com>
41. **[05-01 12:57]** Re: [PATCH v8 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Gavin Shan <gshan@redhat.com>
42. **[05-01 12:59]** Re: [PATCH v8 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Gavin Shan <gshan@redhat.com>
43. **[05-01 13:01]** Re: [PATCH v8 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm
 guests
   - 发件人: Gavin Shan <gshan@redhat.com>
44. **[05-01 13:04]** Re: [PATCH v8 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Gavin Shan <gshan@redhat.com>
45. **[05-01 13:04]** Re: [PATCH v8 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user
 space
   - 发件人: Gavin Shan <gshan@redhat.com>
46. **[05-01 13:06]** Re: [PATCH v8 43/43] KVM: arm64: Allow activating realms
   - 发件人: Gavin Shan <gshan@redhat.com>
47. **[05-01 13:36]** Re: [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
48. **[05-01 13:40]** Re: [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
49. **[05-01 13:40]** Re: [PATCH v8 34/43] arm64: RME: Propagate number of breakpoints and
 watchpoints to userspace
   - 发件人: Gavin Shan <gshan@redhat.com>
50. **[05-01 13:42]** Re: [PATCH v8 36/43] arm64: RME: Initialize PMCR.N with number
 counter supported by RMM
   - 发件人: Gavin Shan <gshan@redhat.com>
51. **[05-01 13:50]** Re: [PATCH v8 37/43] arm64: RME: Propagate max SVE vector length from
 RMM
   - 发件人: Gavin Shan <gshan@redhat.com>
52. **[05-01 13:50]** Re: [PATCH v8 38/43] arm64: RME: Configure max SVE vector length for
 a Realm
   - 发件人: Gavin Shan <gshan@redhat.com>
53. **[05-01 14:31]** Re: [PATCH v8 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
54. **[05-01 14:31]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
55. **[05-01 14:44]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
56. **[05-01 14:47]** Re: [PATCH v8 06/43] arm64: RME: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
57. **[05-01 16:09]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>
58. **[05-01 16:11]** Re: [PATCH v8 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>
59. **[05-01 17:00]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
60. **[05-01 17:50]** Re: [PATCH v8 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
61. **[05-01 17:51]** Re: [PATCH v8 12/43] KVM: arm64: vgic: Provide helper for number of
 list registers
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
62. **[05-02 09:30]** Re: [PATCH v8 39/43] arm64: RME: Provide register list for
 unfinalized RME RECs
   - 发件人: Gavin Shan <gshan@redhat.com>
63. **[05-02 09:41]** Re: [PATCH v8 40/43] arm64: RME: Provide accurate register list
   - 发件人: Gavin Shan <gshan@redhat.com>
64. **[05-02 09:59]** Re: [PATCH v8 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Gavin Shan <gshan@redhat.com>
65. **[05-02 10:46]** Re: [PATCH v8 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Gavin Shan <gshan@redhat.com>
66. **[05-02 12:04]** Re: [PATCH v8 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
67. **[05-02 13:22]** Re: [PATCH v8 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 2: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling

**📧 邮件数**: 44 | **👥 参与者**: 4 | **📅 开始时间**: Sat, 26 Apr 2025 13:27:54 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的细粒度陷阱处理的改进，具体是针对一系列补丁（PATCH v3 00/42）的讨论。

1. **原始补丁内容**：补丁系列旨在重构 KVM 的细粒度陷阱处理，增加对新特性的支持，并修复现有代码中的问题。补丁内容涵盖了多个系统寄存器的添加、更新和错误修复，特别是与 FEAT_LS64 和 FGT2 相关的寄存器。

2. **之前讨论要点**：历史讨论中，Marc Zyngier 提到补丁的规模显著增加，强调尽快合并或放弃该系列补丁。讨论中还提到了一些寄存器的描述更新和新特性支持的必要性。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁合并后的测试问题上。Ganapatrao Kulkarni 报告了在运行自测时遇到的陷阱问题，Marc Zyngier 则指出测试代码的缺陷，并建议对测试进行修改以避免不必要的陷阱。此外，参与者们对补丁中的一些细节进行了审查和修正，包括拼写错误和代码逻辑的清晰度，确保补丁的质量和准确性。整体来看，本周的讨论推动了补丁的进一步完善和测试的改进。

#### 📝 邮件列表

1. **[04-26 13:27]** [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[04-26 13:27]** [PATCH v3 01/42] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64 encoding for FEAT_LS64WB
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-26 13:27]** [PATCH v3 02/42] arm64: sysreg: Update ID_AA64MMFR4_EL1 description
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-26 13:27]** [PATCH v3 03/42] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-26 13:27]** [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with HFG{R,W}TR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-26 13:28]** [PATCH v3 08/42] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-26 13:28]** [PATCH v3 09/42] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-26 13:28]** [PATCH v3 13/42] arm64: Add syndrome information for trapped LD64B/ST64B{,V,V0}
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-26 13:28]** [PATCH v3 16/42] KVM: arm64: Simplify handling of negative FGT bits
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-26 13:28]** [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64* instructions
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-26 13:28]** [PATCH v3 18/42] KVM: arm64: Restrict ACCDATA_EL1 undef to FEAT_ST64_ACCDATA being disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-26 13:28]** [PATCH v3 21/42] KVM: arm64: Compute FGT masks from KVM's own FGT tables
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-26 13:28]** [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-26 13:28]** [PATCH v3 28/42] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[04-26 13:28]** [PATCH v3 40/42] KVM: arm64: Allow sysreg ranges for FGT descriptors
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[04-26 13:28]** [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[04-29 00:03]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
18. **[04-28 22:42]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[04-29 08:34]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[04-29 14:07]** Re: [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with
 HFG{R,W}TR_EL2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[04-29 14:07]** Re: [PATCH v3 09/42] arm64: sysreg: Add registers trapped by
 HDFG{R,W}TR2_EL2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[04-29 14:08]** Re: [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64*
 instructions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[04-29 14:08]** Re: [PATCH v3 18/42] KVM: arm64: Restrict ACCDATA_EL1 undef to
 FEAT_ST64_ACCDATA being disabled
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[04-29 14:08]** Re: [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain
 traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[04-29 14:08]** Re: [PATCH v3 40/42] KVM: arm64: Allow sysreg ranges for FGT
 descriptors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[04-29 14:09]** Re: [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[04-29 14:34]** Re: [PATCH v3 01/42] arm64: sysreg: Add ID_AA64ISAR1_EL1.LS64
 encoding for FEAT_LS64WB
   - 发件人: Joey Gouly <joey.gouly@arm.com>
28. **[04-29 14:38]** Re: [PATCH v3 02/42] arm64: sysreg: Update ID_AA64MMFR4_EL1
 description
   - 发件人: Joey Gouly <joey.gouly@arm.com>
29. **[04-29 14:49]** Re: [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain traps
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[04-29 15:02]** Re: [PATCH v3 03/42] arm64: sysreg: Add layout for HCR_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
31. **[04-29 15:09]** Re: [PATCH v3 24/42] KVM: arm64: Unconditionally configure fine-grain
 traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[04-29 15:10]** Re: [PATCH v3 09/42] arm64: sysreg: Add registers trapped by HDFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[04-29 15:26]** Re: [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with
 HFG{R,W}TR_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
34. **[04-29 20:00]** Re: [PATCH v3 00/42] KVM: arm64: Revamp Fine Grained Trap handling
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
35. **[04-29 15:30]** Re: [PATCH v3 41/42] KVM: arm64: Add FGT descriptors for FEAT_FGT2
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[05-01 11:11]** Re: [PATCH v3 08/42] arm64: sysreg: Add registers trapped by
 HFG{R,W}TR2_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
37. **[05-01 11:17]** Re: [PATCH v3 13/42] arm64: Add syndrome information for trapped
 LD64B/ST64B{,V,V0}
   - 发件人: Joey Gouly <joey.gouly@arm.com>
38. **[05-01 11:43]** Re: [PATCH v3 16/42] KVM: arm64: Simplify handling of negative FGT
 bits
   - 发件人: Joey Gouly <joey.gouly@arm.com>
39. **[05-01 12:01]** Re: [PATCH v3 17/42] KVM: arm64: Handle trapping of FEAT_LS64*
 instructions
   - 发件人: Joey Gouly <joey.gouly@arm.com>
40. **[05-01 12:32]** Re: [PATCH v3 21/42] KVM: arm64: Compute FGT masks from KVM's own
 FGT tables
   - 发件人: Joey Gouly <joey.gouly@arm.com>
41. **[05-01 14:20]** Re: [PATCH v3 04/42] arm64: sysreg: Replace HGFxTR_EL2 with HFG{R,W}TR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[05-01 14:33]** Re: [PATCH v3 28/42] KVM: arm64: Use KVM-specific HCRX_EL2 RES0 mask
   - 发件人: Joey Gouly <joey.gouly@arm.com>
43. **[05-01 14:46]** Re: [PATCH v3 08/42] arm64: sysreg: Add registers trapped by HFG{R,W}TR2_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
44. **[05-01 14:52]** Re: [PATCH v3 08/42] arm64: sysreg: Add registers trapped by
 HFG{R,W}TR2_EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 3: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags

**📧 邮件数**: 18 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 16 Apr 2025 08:51:05 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中允许使用 VMA（虚拟内存区域）标志进行可缓存的二级映射的补丁（PATCH v3 1/1）。

**原始补丁内容**：
该补丁旨在允许在 arm64 的 KVM 中使用 VMA 标志创建可缓存的 PFNMAP（页框号映射），以提高虚拟机迁移的效率和安全性。

**历史讨论要点**：
在之前的讨论中，参与者们探讨了 KVM 是否需要一个能力标志（KVM_CAP）来指示内核是否支持可缓存的 PFNMAP。部分参与者认为这个标志是有用的，尤其是在虚拟机迁移的场景中。讨论中还提到，若主机不支持写回缓存（FWB），则不应允许创建可缓存的 PFNMAP。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上。Ankit Agrawal 提出，应该在内存区域创建时阻止可缓存的 PFNMAP，并在故障处理时进行相应检查。同时，讨论者们一致认为，应该引入新的 KVM 能力标志来暴露可缓存 PFNMAP 的支持。此外，Jason Gunthorpe 提出需要考虑执行映射的情况，确保 KVM 在处理可缓存 PFNMAP 时不会出现缓存一致性问题。总体来看，参与者们对补丁的方向表示支持，并计划在接下来的工作中进行进一步的调整和完善。

#### 📝 邮件列表

1. **[04-16 08:51]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
2. **[04-22 00:49]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[04-22 10:54]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
4. **[04-22 17:50]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[04-22 14:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
6. **[04-22 14:28]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[04-22 20:35]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
8. **[04-23 11:45]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[04-23 09:02]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
10. **[04-23 13:26]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[04-23 10:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
12. **[04-29 10:47]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
13. **[04-29 14:27]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
14. **[04-29 11:14]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
15. **[04-29 17:03]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
16. **[04-29 13:44]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
17. **[04-29 19:09]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
18. **[04-29 15:19]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>

---

### Thread 4: [PATCH v4 0/5] KVM: lockdep improvements

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 30 Apr 2025 16:30:08 -0400

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（内核虚拟机）的锁依赖性（lockdep）改进，主要集中在对 vCPU 锁定的处理优化。

1. **原始 patch/问题的内容**：
   本次讨论的补丁系列（PATCH v4 0/5）旨在改进 KVM 中对所有 vCPU 的锁定机制，特别是通过引入 `mutex_trylock_nest_lock()` 和 `mutex_lock_killable_nest_lock()` 函数来利用 lockdep 的“嵌套锁”特性，从而解决在处理多个 vCPU 时可能出现的锁依赖警告。

2. **之前讨论要点**：
   在之前的讨论中，参与者提到，现有的锁定机制在 vCPU 数量较多时（如超过 48 个）会导致 lockdep 报告最大锁深度过低的错误。为了解决这个问题，建议使用新的嵌套锁机制来减少重复代码并避免不必要的警告。

3. **本周的新讨论、进展或结论**：
   本周的讨论主要集中在补丁的具体实现和细节上。Maxim Levitsky 提出了多个补丁，分别针对不同架构（如 ARM 和 RISC-V）进行调整，使用新的锁定函数以避免 lockdep 警告。参与者 Marc Zyngier 和 Peter Zijlstra 对补丁提出了改进建议，包括增加锁定断言以确保代码的正确性。最终，大家一致认为这些改进将有助于提高 KVM 的稳定性和性能。

#### 📝 邮件列表

1. **[04-30 16:30]** [PATCH v4 0/5] KVM: lockdep improvements
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
2. **[04-30 16:30]** [PATCH v4 1/5] locking/mutex: implement mutex_trylock_nested
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
3. **[04-30 16:30]** [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
4. **[04-30 16:30]** [PATCH v4 3/5] RISC-V: KVM: switch to kvm_trylock/unlock_all_vcpus
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
5. **[04-30 16:30]** [PATCH v4 4/5] locking/mutex: implement mutex_lock_killable_nest_lock
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
6. **[04-30 16:30]** [PATCH v4 5/5] x86: KVM: SEV: implement kvm_lock_all_vcpus and use it
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
7. **[05-01 09:24]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-01 13:15]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
9. **[05-01 13:44]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[05-01 15:41]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
11. **[05-01 14:55]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[05-02 13:57]** Re: [PATCH v4 5/5] x86: KVM: SEV: implement kvm_lock_all_vcpus and
 use it
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[05-02 13:58]** Re: [PATCH v4 2/5] arm64: KVM: use mutex_trylock_nest_lock when
 locking all vCPUs
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[05-03 12:08]** Re: [PATCH v4 5/5] x86: KVM: SEV: implement kvm_lock_all_vcpus and
 use it
   - 发件人: Peter Zijlstra <peterz@infradead.org>

---

### Thread 5: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36

**📧 邮件数**: 14 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 15 Apr 2025 08:47:10 -0700

#### 🤖 AI 总结

本邮件讨论主题为针对AmpereOne处理器的AC03_CPU_36错误的补丁（PATCH 1/2），旨在解决在异步异常发生时，异常可能被错误路由到错误的异常级别的问题。补丁建议在写入HCR_EL2寄存器时，始终阻止异步异常，以避免此错误。

在历史讨论中，参与者们探讨了该错误的具体情况以及补丁的实现细节。D Scott Phillips提出了补丁，并与Marc Zyngier讨论了在不同模式（如nvhe模式）下该错误是否会发生。Marc指出，在nvhe模式下，由于异步异常始终被屏蔽，因此该错误不会发生。

在本周的新讨论中，D Scott Phillips和Marc Zyngier确认了补丁的有效性，并讨论了KVM的其他相关补丁，特别是关于AArch64支持的处理。Marc Zyngier提出了一系列补丁，旨在防止用户空间禁用AArch64支持，并修复HCRX_EL2寄存器的处理。Ganapatrao Kulkarni对这些补丁表示支持并进行了审核。

总体而言，本周的讨论集中在补丁的确认和KVM相关问题的修复上，推动了对AmpereOne处理器错误的解决方案的进一步完善。

#### 📝 邮件列表

1. **[04-15 08:47]** [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[04-16 08:19]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[04-24 19:02]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum
 AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
4. **[04-27 13:21]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum AC03_CPU_36
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[04-28 09:35]** Re: [PATCH 1/2] arm64: errata: Work around AmpereOne's erratum
 AC03_CPU_36
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
6. **[04-29 12:41]** [PATCH 0/2] KVM: arm64: Make AArch64 support sticky
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[04-29 12:41]** [PATCH 1/2] KVM: arm64: Prevent userspace from disabling AArch64 support at any virtualisable EL
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-29 12:41]** [PATCH 2/2] KVM: arm64: selftest: Don't try to disable AArch64 support
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-30 11:08]** Re: [PATCH 0/2] KVM: arm64: Make AArch64 support sticky
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
10. **[04-30 11:59]** [PATCH 0/2] KVM: arm64: Fix HCRX_EL2.GCSEn handling
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[04-30 11:59]** [PATCH 1/2] KVM: arm64: Properly save/restore HCRX_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-30 11:59]** [PATCH 2/2] KVM: arm64: Kill HCRX_HOST_FLAGS
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-30 10:01]** Re: [PATCH 1/2] KVM: selftests: Add default testfiles for KVM
 selftests runner
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[04-30 14:31]** Re: [PATCH 2/2] KVM: selftests: Create KVM selftest runner
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 6: [PATCH 00/10] KVM: selftests: Convert to kernel-style types

**📧 邮件数**: 13 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  1 May 2025 11:32:54 -0700

#### 🤖 AI 总结

[AI 总结失败: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 220417 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}]
策略: 完整 thread (历史:0 新:13, 182916 tokens)

#### 📝 邮件列表

1. **[05-01 11:32]** [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: David Matlack <dmatlack@google.com>
2. **[05-01 11:32]** [PATCH 01/10] KVM: selftests: Use gva_t instead of vm_vaddr_t
   - 发件人: David Matlack <dmatlack@google.com>
3. **[05-01 11:32]** [PATCH 02/10] KVM: selftests: Use gpa_t instead of vm_paddr_t
   - 发件人: David Matlack <dmatlack@google.com>
4. **[05-01 11:32]** [PATCH 03/10] KVM: selftests: Use gpa_t for GPAs in Hyper-V selftests
   - 发件人: David Matlack <dmatlack@google.com>
5. **[05-01 11:32]** [PATCH 04/10] KVM: selftests: Use u64 instead of uint64_t
   - 发件人: David Matlack <dmatlack@google.com>
6. **[05-01 11:32]** [PATCH 05/10] KVM: selftests: Use s64 instead of int64_t
   - 发件人: David Matlack <dmatlack@google.com>
7. **[05-01 11:33]** [PATCH 06/10] KVM: selftests: Use u32 instead of uint32_t
   - 发件人: David Matlack <dmatlack@google.com>
8. **[05-01 11:33]** [PATCH 07/10] KVM: selftests: Use s32 instead of int32_t
   - 发件人: David Matlack <dmatlack@google.com>
9. **[05-01 11:33]** [PATCH 08/10] KVM: selftests: Use u16 instead of uint16_t
   - 发件人: David Matlack <dmatlack@google.com>
10. **[05-01 11:33]** [PATCH 09/10] KVM: selftests: Use s16 instead of int16_t
   - 发件人: David Matlack <dmatlack@google.com>
11. **[05-01 11:33]** [PATCH 10/10] KVM: selftests: Use u8 instead of uint8_t
   - 发件人: David Matlack <dmatlack@google.com>
12. **[05-01 14:03]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[05-02 11:11]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: Andrew Jones <ajones@ventanamicro.com>

---

### Thread 7: [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 14:07:31 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 平台的 Hyper-V 支持虚拟信任级别（VTL）启动的补丁系列。该补丁集的主要目的是使 Hyper-V 代码能够在 ARM64 架构下支持 VTL 启动，这是虚拟安全模式的一部分。

在历史讨论中，补丁系列经历了多个版本的迭代，主要集中在代码的可读性、功能性和与现有系统的兼容性上。补丁的主要内容包括引入和使用 SMCCC API 来检测 Hyper-V 的存在，更新 Kconfig 以支持 ARM64 的 VTL 模式，以及提供与架构无关的 VTL 检测实现。

在本周的新讨论中，Roman Kisel 提出了补丁的第 9 到 11 个版本，进一步完善了对 VTL 模式的支持，包括：
1. **初始化 VTL 字段**：确保 VMBus 能够在 VTL 模式下正常工作。
2. **报告系统启动时的 VTL**：在内核启动时输出当前的 VTL 信息。
3. **更新设备树绑定**：为 VMBus 添加中断和 DMA 一致性属性，以支持 VTL 模式下的操作。

这些补丁经过了多位开发者的审核，并得到了积极的反馈，表明该系列补丁在实现上是可行的，并且有助于增强 ARM64 平台在 Hyper-V 环境中的功能。

#### 📝 邮件列表

1. **[04-28 14:07]** [PATCH hyperv-next v9 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[04-28 14:07]** [PATCH hyperv-next v9 01/11] arm64: kvm, smccc: Introduce and use API for getting hypervisor UUID
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[04-28 14:07]** [PATCH hyperv-next v9 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[04-28 14:07]** [PATCH hyperv-next v9 03/11] Drivers: hv: Enable VTL mode for arm64
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
5. **[04-28 14:07]** [PATCH hyperv-next v9 04/11] Drivers: hv: Provide arch-neutral implementation of get_vtl()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
6. **[04-28 14:07]** [PATCH hyperv-next v9 05/11] arm64: hyperv: Initialize the Virtual Trust Level field
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[04-28 14:07]** [PATCH hyperv-next v9 06/11] arm64, x86: hyperv: Report the VTL the system boots in
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
8. **[04-28 14:07]** [PATCH hyperv-next v9 07/11] dt-bindings: microsoft,vmbus: Add interrupt and DMA coherence properties
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
9. **[04-28 14:07]** [PATCH hyperv-next v9 08/11] Drivers: hv: vmbus: Get the IRQ number from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
10. **[04-28 14:07]** [PATCH hyperv-next v9 09/11] Drivers: hv: vmbus: Introduce hv_get_vmbus_root_device()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
11. **[04-28 14:07]** [PATCH hyperv-next v9 10/11] ACPI: irq: Introduce acpi_get_gsi_dispatcher()
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
12. **[04-28 14:07]** [PATCH hyperv-next v9 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
13. **[05-02 04:08]** RE: [PATCH hyperv-next v9 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Michael Kelley <mhklinux@outlook.com>

---

### Thread 8: [PATCH 0/3] Two minor fixups around FEAT_E2H0

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 29 Apr 2025 21:27:53 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持 FF-A 1.2 及其新 SEND_DIRECT2 ABI 的一系列补丁。补丁分为三个部分：

1. **原始补丁内容**：
   - 补丁集的主要目标是引入对 FF-A 1.2 规范的支持，特别是新的 SEND_DIRECT2 ABI，使得寄存器 x4-x17 可以用于消息负载。此外，补丁还防止主机使用低于已与虚拟机监控器协商的 FF-A 版本。

2. **之前讨论要点**：
   - 之前的讨论主要集中在 FF-A 版本的兼容性问题上，特别是 FF-A 1.1 版本对 ABI 的破坏，以及如何在主机和监控器之间处理版本协商的问题。补丁还涉及对 SMCCC（Secure Monitor Call Convention）1.2 的支持，以确保与 FF-A 1.2 的兼容性。

3. **本周的新讨论与进展**：
   - 本周的讨论中，参与者确认了第一个补丁已成功应用于 arm64 架构。Per Larsen 提出了对 FF-A 1.2 的支持补丁，并展示了通过 QEMU 启动 Android 和加载 Trusty 作为来宾虚拟机时成功使用 SEND_DIRECT2 ABI 的测试结果。此外，Marc Zyngier 对补丁的格式和作者归属提出了反馈，建议在后续提交中遵循文档要求。最后，Sebastian Ene 建议在补丁系列中添加版本标记和变更日志。

整体来看，本周的讨论推动了对 FF-A 1.2 支持的进一步完善，确保了补丁的有效性和兼容性。

#### 📝 邮件列表

1. **[04-29 21:27]** Re: [PATCH 0/3] Two minor fixups around FEAT_E2H0
   - 发件人: Will Deacon <will@kernel.org>
2. **[05-01 20:49]** [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen <perl@immunant.com>
3. **[05-01 20:52]** [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
4. **[05-01 20:53]** [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Per Larsen <perl@immunant.com>
5. **[05-01 20:55]** [PATCH 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host handler
   - 发件人: Per Larsen <perl@immunant.com>
6. **[05-02 09:47]** Re: [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[05-02 09:49]** Re: [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[05-02 02:21]** [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen <perl@immunant.com>
9. **[05-02 02:21]** [PATCH 1/3] KVM: arm64: Restrict FF-A host version renegotiation
   - 发件人: Per Larsen <perl@immunant.com>
10. **[05-02 02:21]** [PATCH 2/3] KVM: arm64: Bump the supported version of FF-A to 1.2
   - 发件人: Per Larsen <perl@immunant.com>
11. **[05-02 02:21]** [PATCH 3/3] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in host handler
   - 发件人: Per Larsen <perl@immunant.com>
12. **[05-02 10:35]** Re: [PATCH 0/3] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Sebastian Ene <sebastianene@google.com>

---

### Thread 9: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Apr 2025 16:27:07 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（内核虚拟机）在 ARM64 架构下的补丁集，主要是为 EL2（异常级别 2）添加对 UBSAN（未定义行为检测器）的支持。

**原始补丁内容**：
补丁集的目标是使 KVM 在 EL2 模式下能够启用 UBSAN，以便检测潜在的未定义行为。UBSAN 运行在两种模式下：正常模式（提供详细错误信息）和陷阱模式（仅报告错误类型）。由于 EL2 模式无法打印报告，因此选择陷阱模式。

**之前讨论要点**：
在历史讨论中，补丁集的设计考虑了与现有内核 UBSAN 的兼容性，并提出了一个新的 KCONFIG 选项（CONFIG_UBSAN_KVM_EL2），以便在 KVM 的受保护模式下单独启用 UBSAN。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. 引入了 `esr_is_ubsan_brk()` 函数，用于处理 UBSAN 相关的异常。
2. 移除了 `report_ubsan_failure()` 函数中的未使用参数，以适应在超管上下文中调用。
3. 处理 UBSAN 故障的代码已被添加到 KVM 的退出处理程序中。
4. Kees Cook 对补丁进行了审核并表示认可，认为补丁的修改是正确的。

总体来看，本周的讨论推进了补丁集的实现，并得到了积极的反馈，预计将通过适当的维护树合并到内核中。

#### 📝 邮件列表

1. **[04-30 16:27]** [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[04-30 16:27]** [PATCH v2 1/4] arm64: Introduce esr_is_ubsan_brk()
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[04-30 16:27]** [PATCH v2 2/4] ubsan: Remove regs from report_ubsan_failure()
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[04-30 16:27]** [PATCH v2 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[04-30 16:27]** [PATCH v2 4/4] KVM: arm64: Handle UBSAN faults
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[04-30 11:30]** Re: [PATCH v2 1/4] arm64: Introduce esr_is_ubsan_brk()
   - 发件人: Kees Cook <kees@kernel.org>
7. **[04-30 11:30]** Re: [PATCH v2 3/4] KVM: arm64: Introduce CONFIG_UBSAN_KVM_EL2
   - 发件人: Kees Cook <kees@kernel.org>
8. **[04-30 11:31]** Re: [PATCH v2 4/4] KVM: arm64: Handle UBSAN faults
   - 发件人: Kees Cook <kees@kernel.org>
9. **[04-30 11:32]** Re: [PATCH v2 0/4] KVM: arm64: UBSAN at EL2
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 10: [PATCH hyperv-next v8 00/11] arm64: hyperv: Support Virtual Trust Level Boot

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 15:47:02 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于在ARM64架构上支持虚拟信任级别（Virtual Trust Level, VTL）启动的补丁集，主题为“[PATCH hyperv-next v8 00/11] arm64: hyperv: Support Virtual Trust Level Boot”。该补丁集旨在使Hyper-V代码能够在ARM64环境中以VTL模式启动，相关的文档可参考微软的Top-Level Functional Specification。

在历史讨论中，Roman Kisel提出了多个补丁，包括使用SMCCC检测Hyper-V存在性以及更新hyperv-pci驱动以支持在VTL模式下通过设备树获取vPCI MSI IRQ域。这些补丁的讨论中，Michael Kelley提出了对UUID定义位置的建议，并指出某些补丁在构建时可能会导致错误。

在本周的新讨论中，Roman Kisel回应了Michael Kelley关于UUID定义的讨论，解释了Hyper-V与KVM的不同，并表示将修复之前提到的构建错误。整体来看，讨论围绕补丁的实现细节和潜在问题展开，参与者积极互动，推动补丁的完善。

#### 📝 邮件列表

1. **[04-14 15:47]** [PATCH hyperv-next v8 00/11] arm64: hyperv: Support Virtual Trust Level Boot
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
2. **[04-14 15:47]** [PATCH hyperv-next v8 02/11] arm64: hyperv: Use SMCCC to detect hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
3. **[04-14 15:47]** [PATCH hyperv-next v8 11/11] PCI: hv: Get vPCI MSI IRQ domain from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
4. **[04-17 15:27]** RE: [PATCH hyperv-next v8 02/11] arm64: hyperv: Use SMCCC to detect
 hypervisor presence
   - 发件人: Michael Kelley <mhklinux@outlook.com>
5. **[04-17 15:28]** RE: [PATCH hyperv-next v8 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Michael Kelley <mhklinux@outlook.com>
6. **[04-28 12:23]** Re: [PATCH hyperv-next v8 02/11] arm64: hyperv: Use SMCCC to detect
 hypervisor presence
   - 发件人: Roman Kisel <romank@linux.microsoft.com>
7. **[04-28 12:24]** Re: [PATCH hyperv-next v8 11/11] PCI: hv: Get vPCI MSI IRQ domain
 from DeviceTree
   - 发件人: Roman Kisel <romank@linux.microsoft.com>

---

### Thread 11: [PATCH v3 0/4] KVM: lockdep improvements

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 30 Apr 2025 16:23:07 -0400

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（内核虚拟机）锁依赖性（lockdep）改进的补丁系列，主要由 Maxim Levitsky 提出。补丁的核心内容是通过引入 `mutex_trylock_nest_lock()` 和 `mutex_lock_killable_nest_lock()` 函数，改进对所有虚拟 CPU（vCPU）的锁定机制，以消除在 SEV（安全虚拟化）代码中出现的锁依赖性警告，并提高代码的整洁性，减少重复代码。

在历史讨论中，虽然没有具体的补丁提及，但可以推测之前的讨论集中在如何优化 KVM 的锁定机制，以避免在多 vCPU 配置下触发锁依赖性警告。

本周的新讨论包括四个补丁的具体实现：
1. **补丁 1**：在 arm64 架构中使用 `mutex_trylock_nest_lock` 替代传统的锁定方法，以避免触发锁依赖性警告。
2. **补丁 2**：在 RISC-V 架构中切换到新的锁定函数，简化代码。
3. **补丁 3**：实现 `mutex_lock_killable_nest_lock`，以支持在迁移过程中锁定所有 vCPU。
4. **补丁 4**：在 x86 架构中实现 `kvm_lock_all_vcpus`，替代 SEV 的自定义锁定函数。

这些补丁的实施旨在提高 KVM 的锁定效率和稳定性，确保在多架构环境下的兼容性和性能。

#### 📝 邮件列表

1. **[04-30 16:23]** [PATCH v3 0/4] KVM: lockdep improvements
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
2. **[04-30 16:23]** [PATCH v3 1/4] arm64: KVM: use mutex_trylock_nest_lock when locking all vCPUs
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
3. **[04-30 16:23]** [PATCH v3 2/4] RISC-V: KVM: switch to kvm_lock/unlock_all_vcpus
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
4. **[04-30 16:23]** [PATCH v3 3/4] locking/mutex: implement mutex_lock_killable_nest_lock
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
5. **[04-30 16:23]** [PATCH v3 4/4] x86: KVM: SEV: implement kvm_lock_all_vcpus and use it
   - 发件人: Maxim Levitsky <mlevitsk@redhat.com>
6. **[04-30 16:30]** Re: [PATCH v3 0/4] KVM: lockdep improvements
   - 发件人: mlevitsk@redhat.com

---

### Thread 12: [PATCH RFC 0/4] stackleak: Support Clang stack depth tracking

**📧 邮件数**: 5 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  2 May 2025 12:01:23 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Linux 内核的补丁系列，主题为「stackleak: 支持 Clang 堆栈深度跟踪」。该补丁系列的主要目的是将现有的 GCC 插件替换为 Clang 实现，以增强内核的安全性。

**原始补丁/问题内容**：
补丁系列包含四个部分，主要修改了与堆栈泄漏（stackleak）相关的配置和实现，以支持 Clang 的堆栈深度跟踪功能。具体包括重命名配置选项、修改堆栈跟踪函数名称、分离编译标志等。

**之前讨论要点**：
在历史讨论中，参与者探讨了使用 Clang 的新特性来替代现有的 GCC 插件，强调了堆栈深度跟踪的重要性，以及如何通过这些修改提高内核的安全性。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上。Kees Cook 提出了四个补丁，分别是：
1. 将 `CONFIG_GCC_PLUGIN_STACKLEAK` 重命名为 `CONFIG_STACKLEAK`。
2. 将 `stackleak_track_stack` 函数重命名为 `__sanitizer_cov_stack_depth`，以符合 Clang 的命名约定。
3. 将与堆栈泄漏相关的编译标志从 `GCC_PLUGINS_CFLAGS` 中分离出来，形成 `STACKLEAK_CFLAGS`。
4. 连接堆栈泄漏功能与 Clang 的堆栈深度跟踪回调。

这些补丁的提出标志着对内核安全性的进一步增强，并为未来的 Clang 支持奠定了基础。

#### 📝 邮件列表

1. **[05-02 12:01]** [PATCH RFC 0/4] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>
2. **[05-02 12:01]** [PATCH RFC 1/4] stackleak: Rename CONFIG_GCC_PLUGIN_STACKLEAK to CONFIG_STACKLEAK
   - 发件人: Kees Cook <kees@kernel.org>
3. **[05-02 12:01]** [PATCH RFC 2/4] stackleak: Rename stackleak_track_stack to __sanitizer_cov_stack_depth
   - 发件人: Kees Cook <kees@kernel.org>
4. **[05-02 12:01]** [PATCH RFC 3/4] stackleak: Split STACKLEAK_CFLAGS from GCC_PLUGINS_CFLAGS
   - 发件人: Kees Cook <kees@kernel.org>
5. **[05-02 12:01]** [PATCH RFC 4/4] stackleak: Support Clang stack depth tracking
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 13: [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM host model

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 18:38:39 +0200

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM/ARM 的补丁系列，主题为“引入可定制的 aarch64 KVM 主机模型”。该补丁旨在通过命令行直接配置 ID 寄存器，主要是对 ID 寄存器存储的重构，并在此基础上进行了改进和文档更新。

在历史讨论中，Cornelia Huck 提出了补丁的主要变化，包括将 ID 寄存器存储的重构拆分出来，并修复了一些错误。此外，补丁还增加了对可写 ID 寄存器的访问器功能，以便更好地管理和使用这些寄存器。

在本周的新讨论中，Sebastian Ott 对补丁中的某些内容提出了建议，指出“GET_IDREG_WRITABLE”似乎在当前系列中未被使用，并建议可以将其删除，认为这可能是早期重构的遗留物。Cornelia Huck 也对此表示同意，确认该功能并未发挥作用。

总体来看，本周的讨论集中在对补丁细节的审查和优化建议上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[04-14 18:38]** [PATCH v3 00/10] kvm/arm: Introduce a customizable aarch64 KVM host model
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[04-14 18:38]** [PATCH v3 05/10] arm/cpu: accessors for writable id registers
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[04-29 18:27]** Re: [PATCH v3 05/10] arm/cpu: accessors for writable id registers
   - 发件人: Sebastian Ott <sebott@redhat.com>
4. **[04-30 15:48]** Re: [PATCH v3 05/10] arm/cpu: accessors for writable id registers
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 14: [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 15 Apr 2025 10:24:05 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 arm64 KVM 的补丁，旨在用 `str_on_off()` 辅助函数替换重复的三元表达式，以提高代码可读性并确保跟踪点字符串格式的一致性。

在历史讨论中，Seongsu Park 提出了这个补丁，并详细说明了其目的和修改内容。Anshuman Khandual 对该补丁进行了审核并表示支持，认为补丁是合适的。

在本周的新讨论中，Seongsu Park 询问 Anshuman Khandual 是否有任何反馈，重申了他对补丁的信心。Marc Zyngier 对补丁表示认可，认为其合理，但指出由于补丁的性质主要是外观上的改进，因此不急于立即合并。他提到在准备 6.16 版本的补丁时，可能会将其纳入考虑。

总的来说，该补丁得到了初步的支持，但尚需等待进一步的合并时机。

#### 📝 邮件列表

1. **[04-15 10:24]** [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper
   - 发件人: Seongsu Park <sgsu.park@samsung.com>
2. **[04-15 12:06]** Re: [PATCH] arm64: kvm: Replace ternary flags with str_on_off()
 helper
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[04-28 16:11]** RE: [PATCH] arm64: kvm: Replace ternary flags with str_on_off()
 helper
   - 发件人: Seongsu Park <sgsu.park@samsung.com>
4. **[04-28 11:04]** Re: [PATCH] arm64: kvm: Replace ternary flags with str_on_off() helper
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 15: [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 24 Apr 2025 19:47:41 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 AmpereOne 处理器的错误 AC04_CPU_23 的补丁（PATCH v2），旨在通过在 HCR_EL2 寄存器的存储操作前后添加 DSB 和 ISB 指令，防止由于并发翻译导致的数据地址访问错误。

在历史讨论中，D Scott Phillips 提出了该补丁的背景，指出在特定条件下，更新 HCR_EL2 可能会导致数据地址的翻译被破坏。补丁通过适当的屏障指令来解决这一问题。

在本周的新讨论中，Marc Zyngier 提出了对补丁的担忧，认为在计算系统能力之前，某些访问可能会受到影响。他建议默认启用该补丁的工作方式，只有在确认系统正常后再放宽限制。此外，他还提到在 C 代码之前的早期代码（如 head.S 和 hyp-stub.S）可能也会受到此问题的影响，建议将这一点记录在相关文档中。D Scott Phillips 认可了这一观点，并表示将进一步检查所有相关代码，而不仅限于 C 代码。

总体来看，本周的讨论集中在补丁的适用性和潜在影响上，参与者对确保系统稳定性表示关注。

#### 📝 邮件列表

1. **[04-24 19:47]** [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>
2. **[04-30 16:53]** Re: [PATCH v2] arm64: errata: Work around AmpereOne's erratum AC04_CPU_23
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[05-01 08:17]** Re: [PATCH v2] arm64: errata: Work around AmpereOne's erratum
 AC04_CPU_23
   - 发件人: D Scott Phillips <scott@os.amperecomputing.com>

---

### Thread 16: [PATCH] KVM: selftests: add test for SVE host corruption

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 17 Apr 2025 00:32:49 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 的自测试补丁，旨在验证 SVE（Scalable Vector Extension）主机状态是否存在被丢弃的问题。该补丁由 Mark Brown 提交，基于 Mark Rutland 原始编写的测试程序，主要用于确保在运行虚拟机时，SVE 寄存器状态不会出现损坏。

在历史讨论中，Mark Brown 提到之前的补丁（提交 ID: fbc7e61195e2）已修复了 KVM 在某些情况下意外丢弃 SVE 状态的问题。该测试程序通过运行简单的虚拟机并检查 SVE 寄存器状态来验证这一点。

在本周的新讨论中，Mark Rutland 对补丁提出了一些细微的修改建议，指出当前测试可能无法完全验证问题的缺失，因为在某些情况下可能会被抢占所掩盖。他建议在测试中尝试操控 SVE 状态，以更好地触发可能的问题。此外，他提到补丁的签名顺序出现了问题，并表示支持该补丁。Mark Brown 随后确认了这些修改，并表示将更新提交信息。

总体来看，本周的讨论主要集中在补丁的细节修改和确认支持上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[04-17 00:32]** [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[04-29 16:27]** Re: [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[04-30 09:48]** Re: [PATCH] KVM: selftests: add test for SVE host corruption
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 17: [PATCH V2] arm64/mm: Implement pte_po_index() for permission overlay index

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 15 Apr 2025 11:14:42 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构中实现 `pte_po_index()` 函数，以支持权限覆盖索引的补丁（PATCH V2）。该补丁的背景是，之前的 `pte_access_permitted()` 函数直接使用 `FIELD_GET()` 来从页表条目（pte）中获取权限覆盖索引，但 `FIELD_GET()` 不支持 128 位数据类型。为了支持即将添加的 D128 页表，提出了创建一个专门的辅助函数 `pte_po_index()`。

在历史讨论中，Ryan Roberts 提出了这个补丁，并指出其目的是为了修复在 Anshuman Khandual 的私有分支中添加 D128 页表支持时出现的一个问题。

在本周的新讨论中，Will Deacon 对补丁提出了一些疑问，表示目前看到的补丁较为零散，难以判断如何处理，并建议可能需要为 KVM 页表代码添加对 128 位类型的支持，而不是避免使用 `FIELD_*` 宏。Ryan Roberts 进一步澄清了补丁的背景，指出 D128 支持尚未准备好提交到主线，并强调在 KVM 需求明确之前，不应发布相关补丁。

总体来看，本周的讨论集中在对补丁的适用性和未来方向的探讨，尤其是在 KVM 方面的考虑。

#### 📝 邮件列表

1. **[04-15 11:14]** [PATCH V2] arm64/mm: Implement pte_po_index() for permission overlay index
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[04-29 16:11]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Will Deacon <will@kernel.org>
3. **[04-29 17:45]** Re: [PATCH V2] arm64/mm: Implement pte_po_index() for permission
 overlay index
   - 发件人: Ryan Roberts <ryan.roberts@arm.com>

---

### Thread 18: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 15:47:10 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH v2 1/6），该补丁旨在为 EL0/1 中使用 FEAT_{LS64, LS64_V} 提供基本的 EL2 设置。

在历史讨论中，补丁的主要内容是确保在 KVM 客户端切换时，HCRX 的设置能够正确生效。参与者 Yicong Yang 提出了对 HCRX 设置在切换到 KVM 客户端时的持续性问题，认为当前的实现可能存在缺陷，特别是在返回主机时会恢复 HCRX_HOST_FLAGS，这可能导致 GCS 代码出现问题。

在本周的新讨论中，Will Deacon 对 Yicong Yang 的问题进行了回应，确认了对 HCRX 设置的关注，并指出可能存在的破坏性影响。同时，他对补丁中的标签名称表示认可，认为这些名称是合适的。整体来看，本周的讨论主要集中在补丁的实现细节及其在 KVM 环境中的表现，参与者们对补丁的有效性和潜在问题进行了深入探讨。

#### 📝 邮件列表

1. **[04-29 15:47]** Re: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1
   - 发件人: Will Deacon <will@kernel.org>
2. **[04-29 15:47]** Re: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 19: [PATCH v2 0/7] Move pKVM ownership state to hyp_vmemmap

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 16 Apr 2025 15:26:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是将 pKVM 的所有权状态迁移到 hyp_vmemmap，主要由 Quentin Perret 提出并在历史邮件中详细阐述。该补丁系列的主要目标是提高超管状态查找的效率，避免了对 hyp 阶段-1 页表的遍历，同时解耦了超管状态与线性映射范围内映射的存在，从而简化现有代码并为未来特性（如 hyp 跟踪）的引入铺平道路。

在历史讨论中，Quentin 提出了补丁的两个主要好处，并介绍了补丁的结构，尽管邮件内容较长，但整体意图明确。

在本周的新讨论中，Marc Zyngier 确认已将该补丁系列应用到下一个版本，并列出了每个补丁的提交信息，包括跟踪 SVE 状态、修复 pKVM 页跟踪注释、引入帮助函数、迁移 hyp 状态等。这表明该补丁系列得到了认可并将继续推进。

#### 📝 邮件列表

1. **[04-16 15:26]** [PATCH v2 0/7] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Quentin Perret <qperret@google.com>
2. **[04-29 14:41]** Re: [PATCH v2 0/7] Move pKVM ownership state to hyp_vmemmap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH for-10.1 v5 00/13] arm: rework id register storage

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 18:43:50 +0200

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 ARM 架构的 ID 寄存器存储的重构补丁（patch）[PATCH for-10.1 v5 00/13]。该补丁旨在优化和改进 ID 寄存器的存储方式。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁经过了初步的审查和讨论，可能涉及到一些技术细节和实现方式的调整。

在本周的新讨论中，参与者 Eric Auger 和 Cornelia Huck 进行了进一步的交流。Cornelia 提到她再次审查了补丁，并指出了一些转换错误，表示由于她是共同作者，无法直接给出认可（R-b）。Eric 对此表示理解，并承认可能是自己造成的错误。随后，Eric 修复了这些问题，并对代码进行了调整，特别是将某些数组引用进行了简化。他计划在进行测试后重新发布补丁。

总体来看，本周的讨论集中在补丁的细节修正和审查反馈上，显示出团队对代码质量的重视和协作精神。

#### 📝 邮件列表

1. **[04-28 18:43]** Re: [PATCH for-10.1 v5 00/13] arm: rework id register storage
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 12:05]** Re: [PATCH for-10.1 v5 00/13] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 21: [PATCH for-10.1 v5 08/13] arm/cpu: Store id_isar0-7 into the
 idregs array

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 18:04:36 +0200

#### 🤖 AI 总结

本邮件线程讨论的是一项针对 ARM CPU 的补丁，主题为“将 id_isar0-7 存储到 idregs 数组中”。该补丁旨在改进 ARM 架构中 ID 寄存器的存储方式。

在历史讨论中，未提供具体的背景信息，因此我们无法得知补丁的详细内容或之前的讨论要点。

在本周的新讨论中，Eric Auger 和 Cornelia Huck 进行了互动。Eric Auger 对补丁中的某个实现表示不满，指出应使用 `SET_IDREG(isar, ID_ISAR5, 0x0);` 的方式来设置 ID 寄存器，而不是当前的实现。Cornelia Huck 随后回应，表示对补丁中某些内容感到困惑，并承诺将进行修正。

总体来看，本周的讨论集中在补丁的具体实现细节上，参与者们对如何正确设置 ID 寄存器进行了探讨，并计划对补丁进行必要的修正。

#### 📝 邮件列表

1. **[04-28 18:04]** Re: [PATCH for-10.1 v5 08/13] arm/cpu: Store id_isar0-7 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:51]** Re: [PATCH for-10.1 v5 08/13] arm/cpu: Store id_isar0-7 into the
 idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 22: [PATCH for-10.1 v5 06/13] arm/cpu: Store aa64dfr0/1 into the
 idregs array

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 17:56:28 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM CPU 的补丁，旨在将 `aa64dfr0` 和 `aa64dfr1` 寄存器的值存储到 `idregs` 数组中。该补丁的目的是增强 ARM 架构的寄存器管理，以便更好地支持虚拟化和相关功能。

在之前的讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了修复或改进现有的寄存器处理逻辑，可能涉及到对 ARM CPU 特性的支持。

在本周的新讨论中，Eric Auger 指出补丁中存在一行代码重复的问题，Cornelia Huck 随后确认了这一点并表示将进行修复。这表明该补丁在提交前需要进一步的审查和修改，以确保代码的正确性和有效性。

总体来看，本周的讨论集中在补丁的细节修正上，参与者们积极沟通，确保最终提交的代码质量。

#### 📝 邮件列表

1. **[04-28 17:56]** Re: [PATCH for-10.1 v5 06/13] arm/cpu: Store aa64dfr0/1 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:48]** Re: [PATCH for-10.1 v5 06/13] arm/cpu: Store aa64dfr0/1 into the
 idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 23: [PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the
 idregs array

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 17:39:28 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM CPU 的补丁，旨在将 aa64pfr0 和 aa64pfr1 寄存器的值存储到 idregs 数组中。补丁的编号为 [PATCH for-10.1 v5 04/13]。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改进 ARM 架构下的寄存器管理，确保相关寄存器的值能够被正确存储和访问。

在本周的新讨论中，参与者 Eric Auger 和 Cornelia Huck 对补丁中的寄存器定义提出了问题。Eric 指出在补丁中存在转换错误，具体体现在 ID_PFR0_EL1 和 ID_PFR1_EL1 的定义上。Cornelia 随后确认了这个错误，并表示将进行修正。

总结来看，本周的讨论主要集中在补丁中的寄存器定义错误上，参与者们达成共识，决定对该错误进行修正，以确保补丁的正确性和有效性。

#### 📝 邮件列表

1. **[04-28 17:39]** Re: [PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:38]** Re: [PATCH for-10.1 v5 04/13] arm/cpu: Store aa64pfr0/1 into the
 idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 24: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 28 Apr 2025 16:52:02 +0200

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM 架构的一个补丁，旨在将 `aa64isar0` 和 `aa64zfr0` 存储到 ID 寄存器数组中。补丁的编号为 [PATCH for-10.1 v5 02/13]，主要目的是改进 CPU 的寄存器管理。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁是基于之前的讨论或需求而提出的，可能涉及到 ARM CPU 的寄存器结构和虚拟化相关的优化。

在本周的新讨论中，参与者 Eric Auger 和 Cornelia Huck 进行了简短的交流。Eric 提到可以在补丁中添加 KVM 相关的内容，并建议在其他调用中使用文件描述符（fd）而不是 `fdarray[2]`，但这可以在后续版本中处理。Cornelia 则回应说，考虑到该系列补丁需要重新调整（respin），可以顺便进行这些修改。

总体来看，本周的讨论主要集中在补丁的细节改进和后续版本的调整上，显示出参与者对代码质量和维护性的关注。

#### 📝 邮件列表

1. **[04-28 16:52]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0 into
 the idregs arrays
   - 发件人: Eric Auger <eric.auger@redhat.com>
2. **[04-29 11:31]** Re: [PATCH for-10.1 v5 02/13] arm/cpu: Store aa64isar0/aa64zfr0
 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 25: [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu,  1 May 2025 16:24:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `host_stage2_set_owner_locked()` 函数中的内存检查错误。

**原始补丁内容**：
补丁由 Mostafa Saleh 提出，主要修复了在 `host_stage2_set_owner_locked()` 函数中对内存地址的检查逻辑。原代码使用 `addr_is_memory(addr)` 进行检查，但该方法不够准确，可能导致内核崩溃。补丁将其修改为 `range_is_memory(addr, addr + size)`，以确保检查的地址范围是有效的内存。

**之前的讨论要点**：
本邮件线程没有历史讨论，所有内容均为本周的新讨论。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的提出和修复内容上。Mostafa Saleh 发现了这个简单的错误，并指出该问题在准备 pKVM 补丁时被注意到。虽然他认为这个错误在正常情况下不会造成严重后果，但如果系统出现异常，仍可能导致内核崩溃。补丁已提交，期待进一步的审查和反馈。

#### 📝 邮件列表

1. **[05-01 16:24]** [PATCH] KVM: arm64: Fix memory check in host_stage2_set_owner_locked()
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 26: [PATCH] arm64: Expose AIDR_EL1 via sysfs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 21:27:51 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 arm64 架构的补丁，旨在通过 sysfs 接口暴露 AIDR_EL1 寄存器的信息。该补丁的目的是增强对 ARM64 CPU 特性的可访问性，便于开发者和用户获取相关信息。

在历史讨论中，没有提供具体的补丁内容或背景信息，可能是因为这是首次提交的补丁，因此缺乏前期的讨论记录。

在本周的新讨论中，参与者 Will Deacon 确认已将该补丁应用于 arm64 的开发分支（for-next/cpufeature），并表示感谢。这表明补丁已经获得了认可并进入了下一步的开发流程。

总结来说，该补丁的目标是提升 ARM64 系统的可用性，虽然没有历史讨论的详细背景，但本周的进展显示出补丁已成功被采纳。

#### 📝 邮件列表

1. **[04-29 21:27]** Re: [PATCH] arm64: Expose AIDR_EL1 via sysfs
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 27: [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 12:43:26 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在强制在 VHE（Virtualization Host Extensions）模式下始终将 HCR_EL2.xMO 设置为 1。

**原始补丁内容**：
该补丁的主要目的是在 VHE 模式下，永久设置 HCR_EL2.xMO 位，以确保物理中断能够正常传递到主机，同时解决两个主要问题：一是当这些位被清除时，可能会阻止 IRQ（中断请求）的处理；二是清除这些位时会触发 AmpereOne 硬件的错误（AC03_CPU_36），导致系统崩溃。

**之前讨论要点**：
在补丁提出之前，讨论主要集中在 HCR_EL2.xMO 位的动态设置和清除上，认为这种做法没有必要，因为在 VHE 模式下，始终希望物理中断能够到达主机。

**本周新讨论与进展**：
本周，Marc Zyngier 提出了补丁的具体实现细节，强调在 VHE 模式下不再动态修改 HCR_EL2.xMO 位，而是直接将其设置为 1。补丁的实现涉及对相关代码路径的修改，但在初始化阶段仍保留早期设置，以避免在中断禁用时出现问题。该补丁已得到 D Scott Phillips 的报告支持，并由 Marc Zyngier 签署。整体来看，该补丁旨在简化中断处理逻辑，提高系统稳定性。

#### 📝 邮件列表

1. **[04-29 12:43]** [PATCH v2] KVM: arm64: Force HCR_EL2.xMO to 1 at all times in VHE mode
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 28: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 29 Apr 2025 11:07:28 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH V3），其目的是启用 EL2 对 FEAT_PMUv3p9 的要求。该补丁旨在增强 ARM64 处理器的性能监控能力。

在历史讨论中，并没有提供具体的背景信息或之前的讨论内容，因此我们无法了解该补丁的详细背景或其提出的原因。

在本周的新讨论中，参与者 Anshuman Khandual 提到，该补丁已经与所需的工具 sysreg 补丁一起合并到相关的稳定分支中，并且现在可以在 v6.12.25 和 v6.14.4 版本中找到。这表明该补丁的实施已经完成，并且已成功集成到 Linux 内核的稳定版本中，为 ARM64 处理器的性能监控提供了支持。

#### 📝 邮件列表

1. **[04-29 11:07]** Re: [PATCH V3] arm64/boot: Enable EL2 requirements for FEAT_PMUv3p9
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

### Thread 29: [PATCH for-10.1 v5 13/13] arm/cpu: switch to a generated
 cpu-sysregs.h.inc

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 28 Apr 2025 18:38:04 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM 架构的补丁，旨在将 CPU 系统寄存器的定义切换到一个生成的文件 `cpu-sysregs.h.inc`。该补丁的目的是提高代码的可维护性和可读性。

在历史讨论中，补丁的初步版本已经提交，参与者 Cornelia Huck 对该补丁进行了评审，并表示支持。虽然没有详细的历史讨论记录，但可以推测该补丁的提出是基于对现有代码结构的优化需求。

在本周的新讨论中，Eric Auger 对补丁进行了确认，表示已审核并认可该补丁。这表明补丁得到了积极的反馈，可能会在后续版本中被合并。

总体来看，该补丁的提出及其审核过程显示了社区对 ARM 架构代码质量提升的重视，且当前进展顺利，已获得初步认可。

#### 📝 邮件列表

1. **[04-28 18:38]** Re: [PATCH for-10.1 v5 13/13] arm/cpu: switch to a generated
 cpu-sysregs.h.inc
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 30: [PATCH for-10.1 v5 03/13] arm/cpu: Store aa64isar1/2 into the
 idregs array

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 28 Apr 2025 17:00:41 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM 架构的补丁，标题为“[PATCH for-10.1 v5 03/13] arm/cpu: Store aa64isar1/2 into the idregs array”。该补丁的主要目的是将 aa64isar1 和 aa64isar2 的值存储到 idregs 数组中，以便于后续的处理和访问。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了优化 ARM CPU 的寄存器管理，可能涉及到对 ARM 架构特性的支持。

在本周的新讨论中，参与者 Eric Auger 对补丁进行了反馈，指出了一些小的改进建议，特别是关于代码简化的部分。他提到可以考虑将 `fdarray[2]` 简化为 `fd`，并表示在经过再次阅读后，整体上补丁看起来不错。

总结而言，此次讨论主要集中在补丁的细节优化上，参与者们对补丁的方向表示认可，同时提出了进一步简化代码的建议。

#### 📝 邮件列表

1. **[04-28 17:00]** Re: [PATCH for-10.1 v5 03/13] arm/cpu: Store aa64isar1/2 into the
 idregs array
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 14 Apr 2025 13:40:56 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中处理 MTE（Memory Tagging Extension）支持的问题，特别是 MTE_ASYNC 的声明。

1. **原始 patch/问题内容**：Ben Horgan 提出了一个 RFC PATCH，目的是修复 KVM 在处理 MTE_ASYNC 支持时的错误。当前情况下，当主机的 ID_AA64PFR1_EL1.MTE 为 2 但不支持 MTE_ASYNC 时，虚拟机仍然会错误地将 MTE_ASYNC 声明为支持。该补丁旨在确保只有在实际支持的情况下，才向虚拟机报告 MTE_ASYNC。

2. **之前讨论要点**：在历史讨论中，Ben 提出了两个补丁，分别是隐藏不必要的 MTE_frac 信息以及根据 MTE 能力条件性地掩蔽 MTE_frac。Marc Zyngier 对此表示关注，认为应该谨慎处理 MTE_frac 的传播，以避免未来可能的兼容性问题。

3. **本周的新讨论、进展或结论**：在本周的讨论中，Ben 对 Marc 的建议表示赞同，并提出了更新条件的方案，以确保在特定情况下正确处理 MTE_frac 的值。他计划根据讨论的反馈更新代码，以更好地反映硬件的实际支持情况。

总体而言，此次讨论集中在确保 KVM 在 arm64 架构中准确报告 MTE 支持的能力，以避免虚拟机错误地获取不支持的功能。

#### 📝 邮件列表

1. **[04-14 13:40]** [RFC PATCH 0/3] KVM: arm64: Don't claim MTE_ASYNC if not supported
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[04-14 13:40]** [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[04-27 18:24]** Re: [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on MTE capability
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[04-28 12:26]** Re: [RFC PATCH 2/3] KVM: arm64: Make MTE_frac masking conditional on
 MTE capability
   - 发件人: Ben Horgan <ben.horgan@arm.com>

---

