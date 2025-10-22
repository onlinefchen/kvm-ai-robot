# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 09:52:46

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 284
- **总 Thread 数**: 36
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 28 threads (245 邮件)
- **RFC**: 3 threads (8 邮件)
- **Selftest**: 1 threads (1 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Other**: 3 threads (29 邮件)

---

## 📌 PATCH

共 28 个 thread

---

### Thread 1: [PATCH v3 00/22] ARM64 PMU Partitioning

**📧 邮件数**: 33 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 26 Jun 2025 20:04:36 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 PMU（性能监控单元）分区的补丁系列，主要由 Colton Lewis 提出。以下是讨论的主要内容：

1. **原始补丁/问题内容**：补丁系列旨在实现 ARM64 的分区 PMU，允许为虚拟机保留部分计数器，从而减少开销并提高性能。补丁中包括了对 PMU 计数器的管理和访问控制的修改。

2. **之前讨论要点**：早期讨论集中在如何实现 PMU 的分区，特别是如何在 VHE（虚拟化扩展）模式下支持这一特性。参与者讨论了分区 PMU 的实现细节，包括如何处理不同的寄存器访问、事件过滤和中断处理等。

3. **本周的新讨论、进展或结论**：本周的讨论主要围绕补丁的具体实现细节，包括如何在 PMU 分区时处理寄存器的读写、如何设置和清除中断标志、以及如何在 KVM 中添加新的 ioctl 接口以支持 PMU 分区。参与者还讨论了如何确保在分区 PMU 的情况下，虚拟机能够正确访问和使用 PMU 计数器。此外，针对补丁的代码审查中，Marc Zyngier 和 Ben Horgan 提出了对补丁内容的建议和修改意见，强调了代码的清晰性和一致性。

总的来说，本周的讨论进一步细化了 PMU 分区的实现方案，确保了在虚拟化环境下的性能监控功能的有效性和可靠性。

#### 📝 邮件列表

1. **[06-26 20:04]** [PATCH v3 00/22] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-26 20:04]** [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[06-26 20:04]** [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-26 20:04]** [PATCH v3 03/22] KVM: arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-26 20:04]** [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-26 20:04]** [PATCH v3 05/22] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[06-26 20:04]** [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[06-26 20:04]** [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[06-26 20:04]** [PATCH v3 08/22] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[06-26 20:04]** [PATCH v3 09/22] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[06-26 20:04]** [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[06-26 20:04]** [PATCH v3 11/22] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[06-26 20:04]** [PATCH v3 12/22] KVM: arm64: Use physical PMSELR for PMXEVTYPER if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[06-26 20:04]** [PATCH v3 13/22] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[06-26 20:04]** [PATCH v3 14/22] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[06-26 20:04]** [PATCH v3 15/22] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[06-26 20:04]** [PATCH v3 16/22] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[06-26 20:04]** [PATCH v3 17/22] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[06-26 20:04]** [PATCH v3 18/22] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[06-26 20:04]** [PATCH v3 19/22] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[06-26 20:04]** [PATCH v3 20/22] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
22. **[06-26 20:04]** [PATCH v3 21/22] KVM: arm64: Add ioctl to partition the PMU when supported
   - 发件人: Colton Lewis <coltonlewis@google.com>
23. **[06-26 20:04]** [PATCH v3 22/22] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
24. **[06-27 10:04]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[06-27 14:23]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[06-27 14:31]** Re: [PATCH v3 03/22] KVM: arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[06-27 14:36]** Re: [PATCH v3 09/22] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[06-27 16:01]** Re: [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[06-27 20:45]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
30. **[06-27 20:45]** Re: [PATCH v3 03/22] KVM: arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Colton Lewis <coltonlewis@google.com>
31. **[06-27 20:45]** Re: [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
32. **[06-27 13:55]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
33. **[06-28 09:25]** Re: [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v6 00/28] KVM: arm64: Implement support for SME

**📧 邮件数**: 31 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 11:47:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构上实现对 SME（可扩展矩阵扩展）的支持，主要包括一系列补丁的提交和反馈。

1. **原始补丁内容**：
   本系列补丁（PATCH v6 00/28）旨在为 KVM 实现对 SME 的支持，特别是在非保护的 KVM 客户端中。补丁中介绍了 SME 的用户空间 ABI、控制寄存器、向量长度配置以及与 SVE（可扩展向量扩展）的交互。

2. **之前的讨论要点**：
   在之前的讨论中，参与者们对 SME 的实现细节进行了深入探讨，特别是如何处理与 SVE 的重叠以及如何管理寄存器的访问和状态。讨论还涉及到如何在 KVM 中配置和启用 SME 特性，以及如何处理相关的异常和陷阱。

3. **本周的新讨论与进展**：
   本周的讨论主要集中在补丁的具体实现和反馈上。Mark Brown 提出了对用户空间访问 SME 特定寄存器的支持、上下文切换 SME 状态的实现、以及如何处理 SME 的异常。Marc Zyngier 对某些寄存器的设计提出了质疑，认为某些寄存器的存在没有必要，并建议在实现中应确保寄存器的状态符合预期。此外，补丁还增加了对 SME 优先级寄存器的支持，并讨论了如何在嵌套客户机中暴露 SME 状态。

总体而言，本周的讨论促进了对 SME 支持的进一步完善，确保了 KVM 在处理 SME 时的正确性和一致性。

#### 📝 邮件列表

1. **[06-25 11:47]** [PATCH v6 00/28] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[06-25 11:47]** [PATCH v6 01/28] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[06-25 11:47]** [PATCH v6 02/28] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[06-25 11:47]** [PATCH v6 03/28] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[06-25 11:47]** [PATCH v6 04/28] arm64/fpsimd: Determine maximum virtualisable SME
 vector length
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[06-25 11:47]** [PATCH v6 05/28] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[06-25 11:47]** [PATCH v6 06/28] KVM: arm64: Pay attention to FFR parameter in SVE
 save and load
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[06-25 11:47]** [PATCH v6 07/28] KVM: arm64: Pull ctxt_has_ helpers to start of
 sysreg-sr.h
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[06-25 11:47]** [PATCH v6 08/28] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[06-25 11:48]** [PATCH v6 09/28] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[06-25 11:48]** [PATCH v6 10/28] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[06-25 11:48]** [PATCH v6 11/28] KVM: arm64: Define internal features for SME
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[06-25 11:48]** [PATCH v6 12/28] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[06-25 11:48]** [PATCH v6 13/28] KVM: arm64: Store vector lengths in an array
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[06-25 11:48]** [PATCH v6 14/28] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
16. **[06-25 11:48]** [PATCH v6 15/28] KVM: arm64: Support SME control registers
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[06-25 11:48]** [PATCH v6 16/28] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Mark Brown <broonie@kernel.org>
18. **[06-25 11:48]** [PATCH v6 17/28] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[06-25 11:48]** [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
20. **[06-25 11:48]** [PATCH v6 19/28] KVM: arm64: Provide assembly for SME register
 access
   - 发件人: Mark Brown <broonie@kernel.org>
21. **[06-25 11:48]** [PATCH v6 20/28] KVM: arm64: Support userspace access to streaming
 mode Z and P registers
   - 发件人: Mark Brown <broonie@kernel.org>
22. **[06-25 11:48]** [PATCH v6 21/28] KVM: arm64: Flush register state on writes to
 SVCR.SM and SVCR.ZA
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[06-25 11:48]** [PATCH v6 22/28] KVM: arm64: Expose SME specific state to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[06-25 11:48]** [PATCH v6 23/28] KVM: arm64: Context switch SME state for guests
   - 发件人: Mark Brown <broonie@kernel.org>
25. **[06-25 11:48]** [PATCH v6 24/28] KVM: arm64: Handle SME exceptions
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[06-25 11:48]** [PATCH v6 25/28] KVM: arm64: Expose SME to nested guests
   - 发件人: Mark Brown <broonie@kernel.org>
27. **[06-25 11:48]** [PATCH v6 26/28] KVM: arm64: Provide interface for configuring and
 enabling SME for guests
   - 发件人: Mark Brown <broonie@kernel.org>
28. **[06-25 11:48]** [PATCH v6 27/28] KVM: arm64: selftests: Add SME system registers
 to get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
29. **[06-25 11:48]** [PATCH v6 28/28] KVM: arm64: selftests: Add SME to set_id_regs
 test
   - 发件人: Mark Brown <broonie@kernel.org>
30. **[06-29 10:32]** Re: [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[06-29 11:08]** Re: [PATCH v6 17/28] KVM: arm64: Support SME identification registers for guests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 26 | **👥 参与者**: 7 | **📅 开始时间**: Wed, 11 Jun 2025 11:47:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 中对 Arm CCA（保密计算架构）支持的补丁（PATCH v9 00/43）。该补丁系列旨在实现受保护虚拟机的运行，相关的客户机支持已在 v6.14-rc1 中合并。

在历史讨论中，Steven Price 提出了多个补丁，涵盖了创建和配置领域、内存运行时故障处理、以及处理领域的进入和退出等功能。讨论中提到了一些代码改进和问题修复，例如 RTT（Realm Translation Table）管理和内存分配的细节。

本周的新讨论中，参与者对补丁进行了进一步的审查和测试。Zhuangyiwei 指出了一些代码中的潜在问题，并得到 Steven 的确认和修正。Emi Kisanuki 报告了在 Fujitsu 内部模拟器上测试补丁的结果，确认了虚拟机的成功启动和大部分测试的通过，除了 PMU（性能监控单元）不被支持。整体来看，补丁的进展顺利，参与者积极提出建议和反馈，推动了补丁的完善。

#### 📝 邮件列表

1. **[06-11 11:47]** [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[06-11 11:48]** [PATCH v9 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
3. **[06-11 11:48]** [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
4. **[06-11 11:48]** [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
5. **[06-11 11:48]** [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
6. **[06-11 11:48]** [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
7. **[06-11 11:48]** [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
8. **[06-11 11:48]** [PATCH v9 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
9. **[06-11 11:48]** [PATCH v9 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
10. **[06-16 11:41]** Re: [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
11. **[06-16 21:55]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
12. **[06-17 20:56]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: zhuangyiwei <zhuangyiwei@huawei.com>
13. **[06-18 13:33]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Andre Przywara <andre.przywara@arm.com>
14. **[06-23 21:17]** Re: [PATCH v9 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: zhuangyiwei <zhuangyiwei@huawei.com>
15. **[06-23 15:45]** Re: [PATCH v9 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>
16. **[06-23 15:45]** Re: [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
17. **[06-23 15:45]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
18. **[06-23 15:45]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
19. **[06-23 17:04]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
20. **[06-24 13:50]** Re: [PATCH v9 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Joey Gouly <joey.gouly@arm.com>
21. **[06-24 16:10]** Re: [PATCH v9 22/43] KVM: arm64: Validate register access for a
 Realm VM
   - 发件人: Joey Gouly <joey.gouly@arm.com>
22. **[06-25 01:45]** RE: [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
23. **[06-25 01:51]** RE: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
24. **[06-25 10:00]** Re: [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
25. **[06-27 11:37]** Re: [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
26. **[06-27 11:37]** Re: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 4: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 20 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 14:33:12 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主要是实现将 guest_memfd 支持的内存映射到主机，以增强软件保护虚拟机的安全性。

**原始补丁内容**：
补丁系列的核心是实现将 guest_memfd 支持的内存映射到主机，特别是针对像 Firecracker 这样的虚拟机监控器（VMM），以增强对 Spectre 类攻击的防护。补丁还涉及对相关内存属性的处理和命名的改进。

**之前讨论要点**：
在历史讨论中，参与者对补丁的命名和功能进行了多次反馈，提出了对某些函数和标志的重命名建议，以提高代码的可读性和一致性。例如，讨论了将 `has_private_mem` 重命名为 `supports_gmem`，以更清晰地表示内存支持情况。

**本周新讨论和进展**：
本周的讨论集中在即将发布的 V13 版本的计划变更上。Fuad Tabba 提出了多个命名和结构的调整建议，包括将 `GUEST_MEMFD_FLAG_SUPPORT_SHARED` 改为 `GUEST_MEMFD_FLAG_MMAP`，并讨论了如何处理支持和不支持 mmap 的 guest_memfd 内存槽的共存问题。David Hildenbrand 和其他参与者对这些变更表示赞同，并讨论了如何简化代码逻辑，以便更好地处理内存属性和故障处理。最终，大家达成共识，计划在 V13 中实施这些变更，并等待其他参与者的反馈。

#### 📝 邮件列表

1. **[06-11 14:33]** [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-11 14:33]** [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-11 14:33]** [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-11 14:33]** [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[06-12 19:38]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
6. **[06-13 13:35]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-13 15:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-24 11:02]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[06-24 12:16]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
10. **[06-24 11:25]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[06-24 13:44]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
12. **[06-24 12:58]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[06-24 10:50]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[06-24 13:51]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Ackerley Tng <ackerleytng@google.com>
15. **[06-24 16:40]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
16. **[06-25 06:33]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to
 kvm->arch.supports_gmem
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
17. **[06-25 09:00]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[06-25 07:07]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[06-25 14:47]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Ackerley Tng <ackerleytng@google.com>
20. **[06-27 08:01]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 5: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts

**📧 邮件数**: 17 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 20 Jun 2025 16:07:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 GICv5 主机上支持 GICv3 客户机的补丁系列，特别是第一个补丁「[PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI interrupts」。该补丁的主要内容是：当 PPI 中断被转发到客户机时，跳过停用操作，仅执行结束中断（EOI），依赖于客户机后续处理来停用虚拟和物理中断。这一做法旨在模拟 GICv3 的原生行为，并为 GICv3 兼容模式的支持奠定基础。

在历史讨论中，参与者探讨了补丁的实现细节及其对 KVM GIC 支持的影响。讨论中提到，当前的实现需要确保转发的 PPI 行为一致，并且在 GICv5 主机上运行 GICv3 客户机时，系统应无缝工作。

在本周的新讨论中，Sascha Bischoff 和其他参与者就补丁的细节进行了进一步的交流，确认了对兼容模式的处理方式，并讨论了在加载路径中处理兼容模式的最佳实践。此外，Lorenzo Pieralisi 对第一个补丁进行了审核并表示通过，确认了补丁的有效性。整体来看，讨论进展顺利，补丁的实现逐步得到认可。

#### 📝 邮件列表

1. **[06-20 16:07]** [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-20 16:07]** [PATCH 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-20 16:07]** [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[06-20 16:07]** [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[06-20 16:07]** [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[06-20 13:20]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-20 13:25]** Re: [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-20 16:02]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-22 13:19]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[06-22 05:37]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[06-23 13:02]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[06-23 13:11]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[06-23 13:12]** Re: [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[06-23 17:14]** Re: [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Lorenzo Pieralisi <lpieralisi@kernel.org>
15. **[06-23 17:21]** Re: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Lorenzo Pieralisi <lpieralisi@kernel.org>
16. **[06-27 09:49]** Re: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[06-27 09:49]** Re: [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 6: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 11 Jun 2025 15:45:03 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中 IOMMU（输入输出内存管理单元）设备发布中断支持的全面改进，涉及的补丁系列为 [PATCH v3 00/62]。

**原始补丁内容**：补丁主要针对 KVM 中的设备发布中断支持进行重构，特别是针对 ARM64 和 AMD SVM（安全虚拟机）架构的改进，包括对 IPI（中断处理程序）虚拟化的管理和错误处理。

**之前讨论要点**：历史讨论中，参与者们关注了多个补丁的细节，特别是如何处理 IPI 虚拟化的启用与禁用，以及在特定 CPU 错误情况下的处理策略。讨论中提到，AMD 17h 系列 CPU 的 erratum #1235 可能导致中断处理失败，因此需要在这些 CPU 上禁用 IPI 虚拟化。

**本周新讨论与进展**：本周的讨论中，Naveen N Rao 对多个补丁进行了审查并给予了认可，特别是对 IPI 虚拟化的处理和相关注释的改进。Sean Christopherson 也对补丁的应用情况进行了更新，确认大部分补丁已应用于 kvm-x86 分支，并对 ARM64 的补丁进行了适当的分离处理，以便于管理依赖关系。

总体来看，本周的讨论主要集中在补丁的审查、确认及对细节的进一步澄清，推动了补丁的最终应用进程。

#### 📝 邮件列表

1. **[06-11 15:45]** [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-11 15:45]** [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set IsRunning
 if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-11 15:45]** [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization if CPU
 has erratum #1235
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-11 15:45]** [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-19 17:01]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
6. **[06-20 07:39]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-23 16:15]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
8. **[06-23 19:35]** Re: [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization
 if CPU has erratum #1235
   - 发件人: Naveen N Rao <naveen@kernel.org>
9. **[06-23 08:30]** Re: [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization if
 CPU has erratum #1235
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-23 21:24]** Re: [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Naveen N Rao <naveen@kernel.org>
11. **[06-23 09:18]** Re: [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[06-24 12:38]** Re: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[06-25 20:58]** Re: [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Naveen N Rao <naveen@kernel.org>

---

### Thread 7: [PATCH v3 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 16:08:59 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于为 Armv8.7 架构添加对 FEAT_{LS64, LS64_V} 的支持及相关测试的补丁（PATCH v3 0/7）。该补丁旨在引入单拷贝原子 64 字节加载和存储指令，具体包括在 CPU 特性列表中识别和启用这些功能，并通过 HWCAP3 和 cpuinfo 向用户空间暴露支持情况。

在历史讨论中，参与者们探讨了如何在虚拟机中处理不支持的内存访问，特别是 LS64 指令引发的数据中断（DABT）。Marc Zyngier 提出用户空间应能够处理这些异常，并建议在某些情况下直接将异常注入回虚拟机。

本周的新讨论中，Yicong Yang 提供了补丁的详细实现，涵盖了如何处理 LS64 指令的 DABT、允许用户空间注入不支持的 DABT、以及在 EL0/1 中的基本设置。参与者们还讨论了如何在虚拟机中处理与 LS64 相关的内存访问异常，Marc Zyngier 建议在某些情况下直接将异常返回给虚拟机，而不是通过 VMM 处理。最终，Yicong Yang 表示将根据讨论结果更新补丁。

整体来看，本周的讨论集中在如何有效地实现和测试这些新特性，以及在虚拟化环境中处理相关异常的最佳实践上。

#### 📝 邮件列表

1. **[06-26 16:08]** [PATCH v3 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[06-26 16:09]** [PATCH v3 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[06-26 16:09]** [PATCH v3 2/7] KVM: arm64: Add documentation for KVM_EXIT_ARM_LDST64B
   - 发件人: Yicong Yang <yangyicong@huawei.com>
4. **[06-26 16:09]** [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[06-26 16:09]** [PATCH v3 4/7] KVM: arm/arm64: Allow user injection of unsupported exclusive/atomic DABT
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[06-26 16:09]** [PATCH v3 5/7] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Yicong Yang <yangyicong@huawei.com>
7. **[06-26 16:09]** [PATCH v3 6/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[06-26 16:09]** [PATCH v3 7/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Yicong Yang <yangyicong@huawei.com>
9. **[06-26 16:11]** Re: [PATCH v3 4/7] KVM: arm/arm64: Allow user injection of
 unsupported exclusive/atomic DABT
   - 发件人: Yicong Yang <yangyicong@huawei.com>
10. **[06-26 09:51]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[06-26 19:39]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64*
 instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
12. **[06-27 14:12]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 20 Jun 2025 17:44:14 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是针对 Linux 内核的一个补丁（PATCH v2 01/23），该补丁旨在为 ARM64 架构添加 HPMN0 的 CPU 特性标识（cpucap）。历史讨论中，Colton Lewis 提出了对补丁描述字段的反馈，认为应该使用更具描述性的名称，而不仅仅是 "FEAT_HPMN0"，以保持一致性。

在本周的新讨论中，Colton Lewis 对之前的反馈表示感谢，并承诺将根据 Oliver Upton 的建议修改描述字段。此外，讨论还涉及到与 PMUv3 驱动相关的其他补丁，Colton 和 Oliver 就如何处理 32 位 ARM 的分区问题进行了深入探讨。Oliver 建议使用一个有符号整数来表示分区行为，以便更清晰地传达用户意图。

总体而言，本周的讨论集中在补丁的描述一致性和 PMU 分区的实现细节上，参与者们积极交流，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[06-20 17:44]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[06-20 18:06]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-23 18:25]** Re: [PATCH v2 03/23] arm64: cpufeature: Add cpucap for PMICNTR
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-23 18:25]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-23 18:26]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-23 22:04]** Re: [PATCH v2 05/23] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[06-23 22:11]** Re: [PATCH v2 17/23] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[06-24 00:05]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-24 00:28]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-24 20:05]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[06-24 20:05]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 9: [PATCH v8 00/14] arm: rework id register storage

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 17 Jun 2025 17:39:17 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM 架构的 ID 寄存器存储重构的补丁（PATCH v8 00/14）。该补丁主要针对 Peter 的反馈进行了改进，确保每个中间阶段都能编译，并增强了脚本的稳健性，确保只抓取所需的寄存器。

在历史讨论中，Cornelia Huck 提到了一些补丁的编译测试结果，并指出了 checkpatch 工具在处理代码时出现的错误，尤其是关于行长度和宏定义的复杂性问题。Eric Auger 也提出了生成系统寄存器定义的脚本，并讨论了如何改进 checkpatch 以减少错误。

在本周的新讨论中，Eric Auger 继续关注 checkpatch 的错误，指出除了之前提到的错误外，还有其他行长度超标的问题。Daniel 认为可以忽略某些错误，因为这些文件不常见。Cornelia Huck 和 Peter Maydell 讨论了是否应该提及故意忽略 checkpatch 的反馈，最终达成共识，认为在某些情况下，保持代码的可读性比严格遵循检查工具的建议更为重要。

总体来看，讨论集中在补丁的改进、代码风格的争议以及如何处理工具反馈的问题上。

#### 📝 邮件列表

1. **[06-17 17:39]** [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-17 17:39]** [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[06-17 17:45]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[06-25 11:10]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Eric Auger <eric.auger@redhat.com>
5. **[06-25 11:16]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Eric Auger <eric.auger@redhat.com>
6. **[06-25 10:23]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
7. **[06-25 11:24]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[06-25 11:31]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Eric Auger <eric.auger@redhat.com>
9. **[06-25 11:14]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
10. **[06-25 18:37]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 10: [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 17:12:20 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）的补丁系列，主要集中在提供一个能力以禁用 APERF/MPERF 读取拦截的功能。

1. **原始补丁内容**：
   该补丁系列的核心是允许虚拟机（VM）读取物理 IA32_APERF 和 IA32_MPERF MSR（模型特定寄存器），而不进行拦截。这使得虚拟机能够在受限环境中获取有效的物理 CPU 频率信息。

2. **之前讨论要点**：
   在之前的讨论中，补丁经历了多个版本的迭代，主要改进了 MSR 拦截的处理方式，并增加了自测试用例以验证新功能的正确性。补丁还整合了对 L2 虚拟机的支持，并确保在自测试中检查 MSR 的可访问性。

3. **本周的新讨论与进展**：
   本周的讨论中，补丁的各个部分得到了进一步的审查和确认。参与者 Xiaoyao Li 对补丁进行了审核并提出了一些小的修改建议。补丁的自测试部分也得到了扩展，以验证在禁用 APERF/MPERF 拦截时，虚拟机和主机之间的 MSR 读取返回严格递增的值。此外，补丁系列还包括对任务绑定 API 的扩展，以便在自测试中更好地管理 CPU 亲和性。

总体而言，本周的讨论集中在补丁的细节审查和自测试的完善上，为最终的合并做好了准备。

#### 📝 邮件列表

1. **[06-25 17:12]** [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-25 17:12]** [PATCH v5 1/5] KVM: x86: Replace growing set of *_in_guest bools with
 a u64
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-25 17:12]** [PATCH v5 2/5] KVM: x86: Provide a capability to disable APERF/MPERF
 read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-25 17:12]** [PATCH v5 3/5] KVM: selftests: Expand set of APIs for pinning tasks
 to a single CPU
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-25 17:12]** [PATCH v5 4/5] KVM: selftests: Test behavior of KVM_X86_DISABLE_EXITS_APERFMPERF
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-25 17:12]** [PATCH v5 5/5] KVM: selftests: Convert arch_timer tests to common
 helpers to pin task
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-26 16:53]** Re: [PATCH v5 1/5] KVM: x86: Replace growing set of *_in_guest bools
 with a u64
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
8. **[06-26 16:59]** Re: [PATCH v5 2/5] KVM: x86: Provide a capability to disable
 APERF/MPERF read intercepts
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>

---

### Thread 11: [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 16 Jun 2025 16:02:41 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的多个补丁，主要集中在 SCTLR2、DoubleFault2 和 NV 外部中止的修复。

**原始 patch/问题的内容**：
Oliver Upton 提出的补丁系列（[PATCH v2 00/27]）旨在实现 FEAT_RAS、FEAT_SCLTR2 和 FEAT_DoubleFault2 的功能，特别是针对非虚拟化（NV）和虚拟化（non-NV）环境中的错误处理机制。这些补丁的核心在于改进 SError 异常的路由和处理，确保在不同上下文中能够正确处理外部中止。

**之前讨论要点**：
在历史讨论中，Marc Zyngier 提出了对补丁的反馈，认为在处理 SError 时，可能不需要进行预取操作，并讨论了如何在 VM 中处理 RAS（Reliability, Availability, and Serviceability）的问题。此外，关于如何在 EASE（External Abort Synchronous Enable）设置时将 SEAs（Synchronous External Aborts）路由到 SError 向量的实现细节也引发了讨论。

**本周的新讨论、进展或结论**：
本周，Oliver Upton 对之前的讨论进行了回应，确认了对 EASE 的理解，并修复了与 kvm_inject_s2_fault() 的关联问题。此外，他强调了在处理 SError 时需要确保 VSE（Virtual SError）标志的正确设置，以避免在 WFI（Wait For Interrupt）仿真中出现阻塞情况。Oliver 还提到将更新 KVM_GET_VCPU_EVENTS 以测试相关标志，以确保补丁的有效性和清晰性。整体来看，补丁的讨论进展顺利，参与者对实现细节达成了一致。

#### 📝 邮件列表

1. **[06-16 16:02]** [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[06-16 16:02]** [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 16:02]** [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[06-21 11:47]** Re: [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[06-21 12:54]** Re: [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[06-24 01:12]** Re: [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector
 when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-24 04:44]** Re: [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing
 / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 12: [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 13 Jun 2025 15:52:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 中为 arm64 架构添加一个属性，以控制 GICD_TYPER2.nASSGIcap。该补丁旨在允许用户空间按虚拟机（VM）基础控制 GICD_TYPER2.nASSGIcap 的支持，从而解决 GIC 架构中对 ITS 能够跟踪的虚拟处理器（vPE）数量的限制。

在历史讨论中，Raghavendra Rao Ananta 提出了该补丁的初衷，强调了在运行多种 VM 的环境中，能够为特定类型的 VM 提供硬件中断注入支持的重要性。同时，Marc Zyngier 提出了一些建议，包括需要明确默认行为以及是否需要在没有 GICv4.1 的情况下仍然公开该属性。

在本周的新讨论中，Oliver Upton 和 Marc Zyngier 继续探讨了如何处理 nASSGIcap 属性的暴露问题。Oliver 认为，公开该能力对于用户空间的有效性是有益的，而 Marc 则担心直接允许用户空间写入 GICD_TYPER2 会带来复杂性。他们讨论了在 vgic_init() 之前是否可以放宽对寄存器的访问限制，或推迟 vPE 的分配，以简化实现。

总体而言，本周的讨论集中在如何平衡属性的可用性与系统复杂性之间，尚未达成最终结论。

#### 📝 邮件列表

1. **[06-13 15:52]** [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[06-13 15:52]** [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[06-21 09:50]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-23 01:40]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[06-23 10:05]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[06-23 02:25]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-23 15:37]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v2 3/5] arm64/sysreg: Add ICH_VCTLR_EL2

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 10:09:01 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的 KVM（Kernel-based Virtual Machine）支持 GICv3（通用中断控制器版本 3）虚拟机在 GICv5（版本 5）主机上运行的补丁系列。主要补丁内容包括添加系统寄存器 ICH_VCTLR_EL2，以支持在 GICv5 主机上启用/禁用 GICv3 兼容模式（FEAT_GCIE_LEGACY）。

在历史讨论中，邮件中并未提及之前的讨论内容，但本周的讨论集中在补丁的具体实现和功能上。Sascha Bischoff 提出了五个补丁，主要包括：
1. **添加 ICH_VCTLR_EL2**：这是一个系统寄存器，用于在 GICv5 主机上启用 GICv3 兼容模式。
2. **填充 gic_kvm_info 结构**：用于 KVM 检测兼容的 GIC。
3. **支持 GICv3 兼容模式**：确保 GICv5 主机能够运行 GICv3 虚拟机。
4. **跳过 PPI 中断的去激活**：在转发 PPI 中断时，跳过去激活操作，依赖虚拟机处理。
5. **探测 GICv5**：添加探测功能，以支持在 GICv5 主机上运行 GICv3 虚拟机。

本周的讨论主要集中在补丁的细节和实现上，参与者们对补丁进行了审查和讨论，确保其功能符合预期。整体来看，这些补丁旨在提升 KVM 在 ARM64 架构上的兼容性和性能，特别是在 GICv5 环境中。

#### 📝 邮件列表

1. **[06-27 10:09]** [PATCH v2 3/5] arm64/sysreg: Add ICH_VCTLR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-27 10:09]** [PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-27 10:09]** [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[06-27 10:09]** [PATCH v2 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[06-27 10:09]** [PATCH v2 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[06-27 10:09]** [PATCH v2 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 14: [PATCH v6 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 07:12:24 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构下支持 FF-A 1.2 及 SEND_DIRECT2 ABI 的一系列补丁（PATCH v6 0/5）。FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁集的主要目的是确保主机不会使用低于与虚拟机管理程序协商的 FF-A 版本，以避免兼容性问题。

在历史讨论中，补丁的背景主要集中在 FF-A 1.2 的支持及其与 SMCCC 1.2 的集成。之前的讨论强调了升级 SMCCC 版本的重要性，以及如何在主机处理程序中实现新的消息接口。

本周的新讨论中，补丁逐步完善，包括：
1. **补丁 1/5**：修正主机版本降级尝试时的返回值，确保版本协商后不被更改。
2. **补丁 2/5**：更新 FF-A 初始化和主机处理程序以使用 SMCCC 1.2，简化实现。
3. **补丁 3/5**：将 FFA_NOTIFICATION_* 接口标记为不支持，防止其通过到可信执行环境（TZ）。
4. **补丁 4/5**：将支持的 FF-A 版本更新为 1.2，以便为实现 1.2 特有的消息接口做准备。
5. **补丁 5/5**：在主机处理程序中支持 FFA_MSG_SEND_DIRECT_REQ2，利用 SMCCC 1.2 的调用约定。

这些补丁的实施将增强 KVM 在 arm64 上的功能，确保更好的兼容性和性能。

#### 📝 邮件列表

1. **[06-27 07:12]** [PATCH v6 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[06-27 07:12]** [PATCH v6 1/5] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[06-27 07:12]** [PATCH v6 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[06-27 07:12]** [PATCH v6 3/5] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[06-27 07:12]** [PATCH v6 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[06-27 07:12]** [PATCH v6 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 15: [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 18:20:43 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于为 arm64 架构支持 FEAT_LSFE（大型系统浮点扩展）的补丁。FEAT_LSFE 是从 v9.5 开始可选的功能，旨在为浮点值提供原子内存操作。由于当前内核没有对该功能的直接需求，补丁的主要目的是为用户空间提供硬件能力标识（hwcap），并允许 KVM 客户端访问相关的 ID 寄存器字段。

在历史讨论中，补丁的背景信息被简要介绍，强调了 FEAT_LSFE 的可选性及其对内核的影响较小。

本周的新讨论中，Mark Brown 提出了三个补丁：
1. **补丁 1**：为 FEAT_LSFE 添加 hwcap，以便用户空间能够发现该特性。
2. **补丁 2**：在 KVM 中暴露 FEAT_LSFE 相关的 ID 寄存器字段，以便虚拟机能够识别该特性。
3. **补丁 3**：在 kselftest 中添加对 LSFE 的测试，确保其在测试中的可用性。

这些补丁的实施将增强对 FEAT_LSFE 的支持，尽管当前内核尚无直接使用该特性的计划。

#### 📝 邮件列表

1. **[06-27 18:20]** [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[06-27 18:20]** [PATCH 1/3] arm64/hwcap: Add hwcap for FEAT_LSFE
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[06-27 18:20]** [PATCH 2/3] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[06-27 18:20]** [PATCH 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 16: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Sat, 21 Jun 2025 04:21:05 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构下将 GPU 设备内存映射为可缓存的补丁（PATCH v9 0/6）。该补丁旨在解决在 Grace Hopper/Blackwell 超级芯片等平台上，GPU 设备内存的缓存一致性问题。当前 KVM 强制将内存映射为 NORMAL 或 DEVICE_nGnRE，这可能导致安全隐患，尤其是在用户空间和 S2 映射之间属性不匹配的情况下。

在之前的讨论中，Ankit Agrawal 提出了两个补丁：第一个补丁（PATCH v9 0/6）旨在将 GPU 设备内存映射为可缓存，以支持 CPU 可访问的缓存一致性；第二个补丁（PATCH v9 3/6）则修复了由于 S1 和 S2 映射属性不匹配而引发的安全漏洞。

在本周的新讨论中，Ankit 提醒参与者对补丁进行审查，而 Will Deacon 则提出了对 arm64 架构中 get_vma_page_shift() 函数的疑虑，指出该函数错误地假设 VM_PFNMAP VMA 是物理连续的，并讨论了如何确保 remap_pfn_range() 函数中的 'prot' 参数在虚拟机中得到正确反映。这表明当前的优化可能存在不安全的隐患。

#### 📝 邮件列表

1. **[06-21 04:21]** [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-21 04:21]** [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-27 05:03]** Re: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
4. **[06-27 14:49]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 17: [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:47:09 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是修复 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的 MI（Message Interrupt）线级别计算问题，具体体现在函数 `vgic_v3_nested_update_mi()` 中。

原始的 patch 由 Wei-Lin Chang 提出，主要是针对 MI 线的状态计算进行了修正。之前的实现使用位与运算直接计算 MI 线状态，可能导致在 vcpu 的 ICH_MISR_EL2 的最低有效位未设置时得出错误结果。修正后的代码在判断 MI 线状态时，确保在 ICH_HCR_EL2.En 设置且 ICH_MISR_EL2 非零的情况下，正确计算 MI 线状态。

在之前的讨论中，Marc Zyngier 对 Wei-Lin Chang 的修正表示赞赏，并提出了进一步优化代码的建议，强调了代码的可读性。

本周的新讨论中，Marc Zyngier 采纳了 Wei-Lin Chang 的修正，并对代码进行了简化，确保逻辑更加清晰。最终，Marc 确认将该 patch 应用到修复补丁中，并感谢了 Wei-Lin Chang 的贡献。该修复已成功提交，标识为 commit `af040a9a296044fd4b748786c2516f172a7617f1`。

#### 📝 邮件列表

1. **[06-25 16:47]** [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[06-25 17:45]** Re: [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-26 13:57]** Re: [PATCH] KVM: arm64: nv: Fix MI line level calculation in
 vgic_v3_nested_update_mi()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[06-26 08:52]** Re: [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 20:41:42 +0800

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构中 HIP10 和 HIP10C 处理器的错误修复补丁，具体是为解决 erratum 162200803 提供的解决方案。该错误涉及 GICv4.0 中的 vPE 调度问题，当多个虚拟处理单元（vPE）同时发送调度命令时，可能会导致某些命令未被调度，从而引发超时。

在本周的讨论中，Zhou Wang 提出了通过限制虚拟本地中断（vLPI）的数量来解决该问题，建议将其限制为 4096，以确保硬件在处理调度操作时不会超出特定值。然而，Marc Zyngier 指出，这一限制在 KVM 中并未得到强制执行，可能导致虚拟机请求超过限制的 vLPI，从而引发问题。他还询问在处理超出限制的 MAPTI 命令时，是否需要通知虚拟机。

Zhou Wang 随后回应，承认在处理 MAPTI/MAPI 命令时缺少对 vLPI 数量的检查，并讨论了在补丁中是否应加入相关检查的必要性。整体来看，本周的讨论集中在补丁的有效性及其潜在的实现问题上。

#### 📝 邮件列表

1. **[06-26 20:41]** [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[06-26 14:27]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-27 14:36]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 19: [PATCH v6] coccinelle: misc: Add field_modify script

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 14:02:20 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个名为「[PATCH v6] coccinelle: misc: Add field_modify script」的补丁，该补丁旨在通过引入 FIELD_MODIFY() 宏来优化内核代码中对字段修改的处理。具体来说，补丁通过 Coccinelle 工具提供了一个脚本（field_modify.cocci），用于查找和建议将原始字段修改模式转换为使用 FIELD_MODIFY() API 的形式，从而在编译时捕获可能的参数类型错误。

在历史讨论中，补丁经历了多个版本的修改，主要集中在简化 Coccinelle 脚本的条件选择、更新文档示例以及移除不必要的 ARM64 补丁等方面。每个版本的更新都通过邮件链接进行了详细记录。

在本周的新讨论中，参与者 Markus Elfring 提出了代码格式化方面的建议，认为使用格式化字符串字面量作为函数调用参数会使代码更加清晰。对此，Luo Jie 表示赞同，并承诺在下一个版本中进行相应的更新。整体来看，本周讨论主要集中在代码的可读性和清晰度上，未涉及其他实质性问题。

#### 📝 邮件列表

1. **[06-26 14:02]** [PATCH v6] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-26 09:43]** Re: [PATCH v6] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
3. **[06-27 12:33]** Re: [PATCH v6] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

### Thread 20: [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 10:10:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，目的是解决在启用 pKVM（保护虚拟机）模式时，GICv2（通用中断控制器版本2）下不应释放 hypervisor 页面的问题。

**原始补丁内容**：
补丁由 Quentin Perret 提交，主要修复了在启用 pKVM 时，KVM 初始化过程中如果出现错误，可能会导致 hypervisor 分配的页面被错误释放，从而引发主机内核崩溃。补丁通过跟踪 pKVM 初始化的 CPU，避免在 `teardown_hyp_mode()` 函数中释放正在使用的页面。

**之前讨论要点**：
在补丁提交之前，Marc Zyngier 报告了启用保护模式时的崩溃问题，指出在 GICv2 下，错误处理路径未能正确处理 pKVM 的情况，导致了潜在的内存访问错误。

**本周的新讨论与进展**：
在本周的讨论中，Quentin 提到在 Juno-r1 上测试补丁后，系统运行正常，未出现崩溃，表明补丁有效。Marc 随后确认已将该补丁应用到修复分支，并感谢 Quentin 的贡献。最终，补丁被成功合并，标识为 commit: 0e02219f9cf4f0c0aa3dbf3c820e6612bf3f0c8c。

#### 📝 邮件列表

1. **[06-26 10:10]** [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2
   - 发件人: Quentin Perret <qperret@google.com>
2. **[06-26 12:26]** Re: [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-26 12:27]** Re: [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Jun 2025 12:30:58 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `init_hyp_mode()` 函数中的错误处理路径。

**原始补丁内容**：
补丁的主要目的是修复在 pKVM 分配 carveout 失败时，错误路径尝试访问未初始化的 SVE（Scalable Vector Extension）状态，导致空指针解引用的问题。

**之前讨论要点**：
在历史讨论中，参与者 Mostafa Saleh 提到在 6.12 版本中观察到了该问题，并指出错误处理路径中的内存释放顺序不正确，必须先释放 SVE 状态再释放每个 CPU 的指针。Quentin Perret 提出了相关的评论，强调了修复的必要性。

**本周的新讨论与进展**：
在本周的讨论中，Mostafa Saleh 提交了补丁 v2，修正了之前的错误并解决了 Quentin 的反馈。Quentin 对补丁进行了审核并表示认可，建议添加修复历史的引用。Marc Zyngier 随后确认该补丁已被应用到修复列表中，并感谢了参与者的贡献。

总体来看，本周的讨论集中在补丁的最终确认和应用上，标志着该问题的解决。

#### 📝 邮件列表

1. **[06-25 12:30]** [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[06-25 12:35]** Re: [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Quentin Perret <qperret@google.com>
3. **[06-26 08:53]** Re: [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: Fix error path in init_hyp_mode()

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 11:33:01 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的错误处理路径修复的补丁。补丁的主要内容是修复在 `init_hyp_mode()` 函数中，如果 pKVM 分配 carveout 失败，后续代码可能会尝试访问未初始化的指针，导致空指针解引用的问题。补丁通过在 `teardown_hyp_mode()` 函数中添加 NULL 检查，确保在释放内存之前确认指针有效，从而避免潜在的崩溃。

在之前的讨论中，Mostafa Saleh 提出了补丁的初步版本，并指出在特定情况下可能会尝试释放 NULL 指针，因此需要添加相应的检查。Quentin Perret 对此提出了疑问，认为 `free_pages()` 在处理 NULL 指针时应该是安全的，并指出问题的根本在于在释放 per-cpu 页面之前，尝试解引用未分配的内存。

本周的新讨论中，Mostafa 对 Quentin 的反馈表示感谢，并承认在测试中未发现释放 NULL 的问题，可能与配置有关。他表示将根据讨论结果在补丁的下一个版本中进行修正。总体来看，讨论集中在如何安全地管理内存释放和指针检查，以确保系统的稳定性。

#### 📝 邮件列表

1. **[06-25 11:33]** [PATCH] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[06-25 12:22]** Re: [PATCH] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Quentin Perret <qperret@google.com>
3. **[06-25 12:25]** Re: [PATCH] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 23: [PATCH v5] coccinelle: misc: Add field_modify script

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 24 Jun 2025 18:26:59 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v5] coccinelle: misc: Add field_modify script”的补丁，该补丁旨在通过引入新的宏 FIELD_MODIFY() 来改进内核代码中字段修改的处理方式。该宏可以在编译时检查参数类型错误，从而提高代码的安全性和可维护性。

在历史讨论中，补丁经历了多个版本的修改，主要集中在简化 Coccinelle 脚本的条件选择、更新文档示例以及移除与 ARM64 相关的补丁。最终版本的补丁包含了一个新的 Coccinelle 脚本 field_modify.cocci，用于自动化转换内核代码中使用 opencoded 字段修改模式的实例。

在本周的新讨论中，参与者 Markus Elfring 提出了一个代码变体建议，以改进警告消息的格式。Luo Jie 对此表示赞同，并计划在下一个版本中采纳这一建议。这表明补丁的开发者对反馈持开放态度，并致力于进一步优化代码质量。

#### 📝 邮件列表

1. **[06-24 18:26]** [PATCH v5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-24 15:54]** Re: [PATCH v5] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
3. **[06-25 14:26]** Re: [PATCH v5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

### Thread 24: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 16:55:48 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于处理 Loongarch 架构中 KCOV 的 `__init` 与内联函数不匹配的问题。历史讨论中，Huacai Chen 提出了一个补丁（PATCH v2 10/14），建议将相关函数标记为 `__init`，而不是 `__always_inline`，以便更好地处理这些不匹配情况。

在本周的新讨论中，Huacai Chen 表示如果没有异议，他将应用这个补丁并进行相应的修改。Kees Cook 对此表示赞同，感谢 Huacai 的工作，并提到他尚未验证该补丁是否确实解决了他所观察到的不匹配问题，但如果看起来没有问题，他支持这个补丁的应用。

总结来看，讨论围绕着如何有效解决 Loongarch 架构中 KCOV 的函数标记问题，经过双方的确认，补丁的应用得到了支持，尽管 Kees 还需进一步验证其效果。

#### 📝 邮件列表

1. **[06-19 16:55]** Re: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
2. **[06-24 20:31]** Re: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
3. **[06-24 18:09]** =?US-ASCII?Q?Re=3A_=5BPATCH_v2_10/14=5D_loongarch=3A_Han?=
 =?US-ASCII?Q?dle_KCOV_=5F=5Finit_vs_inline_mismatches?=
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 25: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 10:55:48 +0000

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: 在主机阶段-2 故障期间正确调整范围”，讨论了在 pKVM 环境下，`host_stage2_adjust_range()` 函数在处理主机阶段-2 故障时的一个问题。该函数的目的是找到适合内存或 MMIO 区域的最大块映射，但其循环条件存在错误，导致可能尝试映射超出单个块所能覆盖的区域。

在之前的讨论中，Quentin Perret 提出了这个问题，指出虽然在实际应用中这种情况较为少见，但并不符合预期行为。为了解决这个问题，他提出了一个补丁，重构了循环逻辑，以修复错误并提高代码可读性。

在本周的新讨论中，Marc Zyngier 对该补丁表示感谢并确认已将其应用于修复中。补丁的提交标识为 e728e705802fec20f65d974a5d5eb91217ac618d，表明该问题已得到解决。整体来看，本周的讨论主要集中在补丁的确认和应用上，未出现新的争议或问题。

#### 📝 邮件列表

1. **[06-25 10:55]** [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Quentin Perret <qperret@google.com>
2. **[06-26 08:53]** Re: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH v3 00/13] KVM: Make irqfd registration globally unique

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 24 Jun 2025 12:38:26 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中 irqfd 注册的全局唯一性问题。原始的补丁（PATCH v3 00/13）旨在确保 irqfd 的注册在全局范围内是唯一的，以避免潜在的冲突和错误。

在之前的讨论中，虽然没有详细记录，但可以推测该补丁的提出是为了改善 KVM 在处理中断请求时的稳定性和可靠性。补丁中包含了多个子补丁，涉及 irqfd 的初始化、锁的管理、事件队列的处理等多个方面，旨在优化 KVM 的中断处理机制。

在本周的新讨论中，参与者 Sean Christopherson 确认已经将补丁应用于 kvm-x86 的中断处理代码，并列出了 13 个相关的子补丁。这些子补丁涵盖了 irqfd 的本地结构使用、SCRU 锁的管理、等待队列的回调初始化、以及对事件fd 的处理等，显示出该补丁的全面性和细致性。整体来看，本周的进展表明该补丁已成功集成，推动了 KVM 的进一步优化。

#### 📝 邮件列表

1. **[06-24 12:38]** Re: [PATCH v3 00/13] KVM: Make irqfd registration globally unique
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 27: [PATCH] arm64: kvm: trace_handle_exit: use string choices helper

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 24 Jun 2025 06:29:47 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构 KVM 的补丁，旨在改进 `trace_handle_exit` 函数的实现。补丁的主要内容是使用字符串选择助手（string choices helper）来替代原有的条件表达式，以提高代码的可读性和可维护性。

在历史讨论中没有相关的背景信息，因此我们无法提供之前的讨论要点。

本周的讨论中，参与者 Kuninori Morimoto 提出了这个补丁，并在邮件中简要说明了补丁的目的，即通过使用字符串选择助手来简化代码。在补丁中，原先的条件表达式 `__entry->is_write ? "write" : "read"` 被替换为 `str_write_read(__entry->is_write)`，这使得代码更加清晰。补丁已包含相应的代码修改，涉及到 `trace_handle_exit.h` 文件的更新。

总体来看，本周的讨论集中在补丁的具体实现上，强调了代码可读性的提升。

#### 📝 邮件列表

1. **[06-24 06:29]** [PATCH] arm64: kvm: trace_handle_exit: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>

---

### Thread 28: [PATCH] arm64: kvm: sys_regs: use string choices helper

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 24 Jun 2025 06:29:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构下 KVM 的系统寄存器代码进行改进的补丁（patch）。该补丁的主要内容是使用字符串选择帮助函数来简化代码中的读写操作的表示方式。

在历史讨论中没有相关的背景信息或之前的讨论记录，因此本次讨论是首次提出该补丁。补丁具体修改了两个文件：`sys_regs.c` 和 `sys_regs.h`，通过引入 `str_write_read` 函数来替代原有的条件判断，从而提高代码的可读性和可维护性。

在本周的新讨论中，Kuninori Morimoto 提出了这一补丁并进行了详细的代码修改说明。补丁的签名也已附上，表明其作者为 Kuninori Morimoto。当前没有其他参与者对此补丁进行评论或提出问题，表明该补丁可能会顺利推进至下一步的审查或合并阶段。整体来看，本周的讨论集中在补丁的具体实现上，未涉及其他问题或争议。

#### 📝 邮件列表

1. **[06-24 06:29]** [PATCH] arm64: kvm: sys_regs: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 15:10:15 +0530

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（内核虚拟机）嵌套虚拟化自测试的补丁（RFC PATCH v2 0/9）。该补丁旨在启用嵌套虚拟化的自测试功能，以便更好地验证虚拟化层的功能和稳定性。

在历史讨论中，参与者们探讨了嵌套虚拟化的实现细节，特别是如何在不同的虚拟化层（如 L1、L2 和 L3）之间切换，以及在自测试中如何利用主机操作系统的支持来运行嵌套的虚拟机代码。Marc Zyngier 提到，当前的测试代码在 EL2（异常级别2）下运行，并讨论了 L1 和 L2 之间的 MMU 表切换问题。

在本周的新讨论中，Ganapatrao Kulkarni 强调了自测试的目标是创建更简单的测试，而不是完全模拟操作系统或完整的虚拟化环境。他提到，虽然实现这些自测试的过程可能复杂，但其目的是验证嵌套虚拟化的正确性。Marc Zyngier 对此表示疑惑，认为在没有操作系统帮助的情况下实现这些自测试将会非常复杂。

总体而言，讨论集中在如何设计有效的嵌套虚拟化自测试，以确保其功能的可靠性和准确性。

#### 📝 邮件列表

1. **[06-19 15:10]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[06-19 12:45]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-23 16:01]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
4. **[06-23 15:11]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC PATCH 1/2] KVM: Add arch hooks for KVM syscore ops

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 23 Jun 2025 14:27:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了两个 RFC 补丁，主要涉及 KVM（内核虚拟机）中的架构钩子和 ARM64 平台的虚拟中断控制器（VGIC）相关问题。

首先，**第一个补丁**（RFC PATCH 1/2）提出在 KVM 中添加架构钩子，以支持 `kvm_shutdown()`、`kvm_suspend()` 和 `kvm_resume()` 的调用。这些钩子允许不同架构在虚拟机关闭、挂起和恢复时执行特定的操作。补丁中新增了相应的函数声明和实现，确保在 KVM 的关机和挂起过程中能够调用这些架构特定的操作。

**第二个补丁**（RFC PATCH 2/2）则聚焦于 ARM64 平台，解决了在使用 kexec 时系统出现黑屏的问题。该问题源于前一个内核中未正确处理的虚拟 LPI（vLPI）待处理表。补丁通过在关机时调用 `kvm_vgic_v3_shutdown()` 函数，确保所有虚拟处理单元（vPE）被正确解除映射，从而避免了内核文本和 initrd 的损坏。

在本周的新讨论中，David Woodhouse 提到之前尝试的一个解决方案未能奏效，并分享了在处理 vLPI 待处理表时的经验教训。他指出，增加几毫秒的延迟能够解决该问题，同时强调了在 DMA 设备后面使用 IOMMU 的重要性，以防止类似问题的再次发生。

总体而言，本周的讨论进一步推动了 KVM 在 ARM64 上的稳定性和可靠性，特别是在处理关机和挂起时的架构特定操作。

#### 📝 邮件列表

1. **[06-23 14:27]** [RFC PATCH 1/2] KVM: Add arch hooks for KVM syscore ops
   - 发件人: David Woodhouse <dwmw2@infradead.org>
2. **[06-23 14:27]** [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>
3. **[06-23 18:38]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

### Thread 3: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 26 Jun 2025 08:22:57 +0200

#### 🤖 AI 总结

本邮件主题为“[RFC] ARM vGIC-ITS tables serialization when running protected VMs”，讨论了在运行受保护虚拟机时，ARM vGIC-ITS 表的序列化问题。

在历史讨论中，David Woodhouse 提出了一个问题，即 KVM 在处理虚拟机状态时，直接将状态写入来宾内存，而不是像正常 KVM 代码那样将其传递给用户空间进行序列化。这种做法在来宾虚拟机从休眠恢复时可能导致 GIC 状态不正确，从而引发内存损坏和后续的虚拟机崩溃。

本周的新讨论中，David Woodhouse 进一步强调了这一问题，指出在来宾恢复后，GIC 可能处于错误状态，导致 KVM 的序列化操作出现内存损坏。他提到，尽管可能将问题归咎于来宾内核，但这种情况仍然是由于 GIC 硬件设计的不合理所致。他呼吁应当为用户空间提供一种正常的序列化 GIC 状态的方法，以避免当前的设计缺陷。

总结来看，讨论集中在 KVM 如何更合理地处理 GIC 状态序列化的问题上，提出了改进的建议以提升系统的稳定性和可靠性。

#### 📝 邮件列表

1. **[06-26 08:22]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 Selftest

共 1 个 thread

---

### Thread 1: kselftest kvm/arm/page_fault_test hangs if pagesize is 16KB

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 15:34:57 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 kselftest 中的 kvm/arm/page_fault_test 测试在页面大小为 16KB 时出现挂起的问题。 

在本周的讨论中，参与者 Itaru Kitayama 提到，当前的 kvm kselftest 中的 page_fault_test 在 QEMU TCG 模式下和 -cpu max 类型时会挂起。邮件中提供了详细的调用栈信息，显示了在执行过程中发生的具体情况。Itaru 还指出，当使用 4KB 和 64KB 的页面大小时，page_fault_test 能正常运行，这表明问题可能与 16KB 页面大小的处理有关。

目前尚未有针对该问题的补丁或解决方案提出，讨论仍在进行中，后续可能需要更多的分析和测试来确定问题的根本原因。

#### 📝 邮件列表

1. **[06-27 15:34]** kselftest kvm/arm/page_fault_test hangs if pagesize is 16KB
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #4

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 26 Jun 2025 16:20:23 +0100

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM/arm64 的修复补丁，旨在为 6.16 版本提供更新。本周的讨论主要由 Marc Zyngier 提出，内容涉及一系列小修复，主要包括以下几点：

1. **原始补丁内容**：本次补丁主要解决了 pKVM 初始化失败时不影响主机运行的问题，确保在主机 S2 中不会映射过多资源，以及修复嵌套 GICv3 模拟中的一个质量缺陷。

2. **之前讨论要点**：历史讨论部分未提供具体内容，因此无法总结之前的讨论要点。

3. **本周的新讨论与进展**：本周的邮件中，Marc Zyngier 提到了一些具体的修复措施，包括：
   - 如果中断控制器不是 GICv3，则优雅地处理 pKVM 初始化失败的情况。
   - 如果 carveout 分配失败，也要优雅地处理 pKVM 初始化失败。
   - 修正主机在 stage-2 故障时所需的最小 MMIO 范围计算。
   - 修复嵌套模式下 GICv3 维护中断的生成问题。

补丁的具体实现涉及多个文件的修改，共计 23 行新增和 13 行删除。这些修复旨在提升 KVM/arm64 的稳定性和性能。

#### 📝 邮件列表

1. **[06-26 16:20]** [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 3 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 21 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:48:00 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM 单元测试中添加对 kvmtool 的支持，具体内容如下：

1. **原始 Patch/问题的内容**：
   本次讨论的核心是 Alexandru Elisei 提出的补丁系列（PATCH v4 00/13），旨在将 kvmtool 集成到 KVM 单元测试的运行脚本中。通过配置选项 `--target=kvmtool`，用户可以自动运行所有测试。

2. **之前的讨论要点**：
   在历史讨论中，补丁的目的是使开发者能够更方便地使用 kvmtool 进行测试。kvmtool 相较于 QEMU 更小且易于修改，运行速度更快，但并非所有测试都能在 kvmtool 上运行。补丁系列中包含多个修订，主要是为了改进脚本的可读性和功能性。

3. **本周的新讨论、进展或结论**：
   本周的讨论主要集中在补丁的具体实现和细节上，包括：
   - 添加了 `kvmtool_params` 参数以支持 kvmtool 的特定语法。
   - 引入了 `disabled_if` 参数，以便在不支持的情况下跳过某些测试。
   - 讨论了如何处理 kvmtool 的默认参数和错误检测。
   - 最终确认了补丁的有效性，并得到了参与者的认可。

通过这些补丁，KVM 单元测试现在能够更好地支持 kvmtool，提升了开发者的测试效率和灵活性。

#### 📝 邮件列表

1. **[06-25 16:48]** [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:48]** [kvm-unit-tests PATCH v4 01/13] run_tests.sh: Document --probe-maxsmp argument
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[06-25 16:48]** [kvm-unit-tests PATCH v4 02/13] scripts: Document environment variables
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[06-25 16:48]** [kvm-unit-tests PATCH v4 03/13] scripts: Refuse to run the tests if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[06-25 16:48]** [kvm-unit-tests PATCH v4 04/13] scripts: Use an associative array for qemu argument names
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[06-25 16:48]** [kvm-unit-tests PATCH v4 05/13] scripts: Add 'kvmtool_params' to test definition
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[06-25 16:48]** [kvm-unit-tests PATCH v4 06/13] scripts: Add support for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[06-25 16:48]** [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[06-25 16:48]** [kvm-unit-tests PATCH v4 08/13] scripts: Add KVMTOOL environment variable for kvmtool binary path
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[06-25 16:48]** [kvm-unit-tests PATCH v4 09/13] scripts: Detect kvmtool failure in premature_failure()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[06-25 16:48]** [kvm-unit-tests PATCH v4 10/13] scripts: Do not probe for maximum number of VCPUs when using kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[06-25 16:48]** [kvm-unit-tests PATCH v4 11/13] scripts/mkstandalone: Export $TARGET
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[06-25 16:48]** [kvm-unit-tests PATCH v4 12/13] scripts: Add 'disabled_if' test definition parameter for kvmtool to use
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
14. **[06-25 16:48]** [kvm-unit-tests PATCH v4 13/13] scripts: Enable kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
15. **[06-26 17:25]** Re: [kvm-unit-tests PATCH v4 03/13] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
16. **[06-26 17:29]** Re: [kvm-unit-tests PATCH v4 04/13] scripts: Use an associative
 array for qemu argument names
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
17. **[06-26 17:34]** Re: [kvm-unit-tests PATCH v4 05/13] scripts: Add 'kvmtool_params' to
 test definition
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
18. **[06-26 17:43]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
19. **[06-26 17:41]** Re: [kvm-unit-tests PATCH v4 05/13] scripts: Add 'kvmtool_params' to
 test definition
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
20. **[06-26 18:42]** Re: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the
 runner script
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
21. **[06-26 17:48]** Re: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the
 runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:43:52 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 KVM 单元测试脚本的重构，特别是关于参数管理的改进。

1. **原始 patch/问题的内容**：
   本次讨论的补丁系列旨在重构 KVM 单元测试脚本中的参数管理，主要是将 `extra_params` 重命名为 `qemu_params`，并引入新的参数 `test_args`。这些更改的目的是为了更好地区分 QEMU 和 kvmtool 的命令行选项，并为将来支持 kvmtool 做准备。

2. **之前讨论要点**：
   在之前的讨论中，参与者提到 `extra_params` 的使用导致了参数的混乱，因此需要一个清晰的替代方案。新的 `qemu_params` 将专门用于 QEMU 的参数，而 `test_args` 则用于传递与虚拟机管理程序无关的参数。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Alexandru Elisei 提交了两个补丁，分别实现了上述参数的重命名和引入。补丁得到了 Andrew Jones 的认可，并表示希望其他架构的维护者也能给予支持。补丁的修改已被审查，且预计将被合并，进一步推动 KVM 单元测试的改进。

#### 📝 邮件列表

1. **[06-25 16:43]** [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:43]** [kvm-unit-tests PATCH 1/2] scripts: unittests.cfg: Rename 'extra_params' to 'qemu_params'
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[06-25 16:43]** [kvm-unit-tests PATCH 2/2] scripts: Add 'test_args' test definition parameter
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[06-26 16:58]** Re: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 3: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 23 Jun 2025 15:22:52 +0200

#### 🤖 AI 总结

本邮件线程讨论了在 KVM（Kernel-based Virtual Machine）中针对 ARM64 架构的 VGIC（Virtual Generic Interrupt Controller） ITS（Interrupt Translation Service）实现中的一个补丁。补丁的主要内容是修改 `vgic_its_ctrl` 函数，使其在处理无效的 KVM_DEV_ARM_VGIC_GRP_CTRL 属性时返回 -ENXIO 错误码，以指示设备未正确配置。

在之前的讨论中，David Woodhouse 提到了一种初步的黑客方法，试图通过 ioctl 调用 `unmap_all_vpes()`，但由于使用了错误的文件描述符而未能成功。Eric Auger 提出，文档中对返回值的描述与当前情况不完全匹配，建议更新文档或更改返回值。

在本周的新讨论中，Eric 对补丁进行了反馈，指出 -ENXIO 错误码的返回在 KVM 的高层描述中是有涵盖的，因此不需要更改。最终，Eric 表示对补丁进行了审核并确认其合理性。

综上所述，本周的讨论主要集中在补丁的合理性和文档一致性上，最终达成了一致意见，认为补丁是合适的。

#### 📝 邮件列表

1. **[06-23 15:22]** KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
2. **[06-24 09:25]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: Eric Auger <eauger@redhat.com>
3. **[06-24 11:01]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
4. **[06-24 11:20]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: Eric Auger <eauger@redhat.com>

---

